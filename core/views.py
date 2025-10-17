# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import LoginSerializer, UserResponseUpdateSerializer
from .models import LoginAttempt,ExamSession
import pytz
from django.utils import timezone
from datetime import datetime, time

IST = pytz.timezone('Asia/Kolkata')

now = timezone.now().astimezone(IST)

# Fixed exam start/end time
exam_start = IST.localize(datetime.combine(datetime(2025, 10, 17), time(9, 55)))
submission_start= IST.localize(datetime.combine(datetime(2025, 10, 17), time(9, 45)))
exam_end   = IST.localize(datetime.combine(datetime(2025, 10, 17), time(10, 10)))
class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        session = ExamSession.objects.filter(user__username=request.data.get('username')).first()
        if session and session.completed:
            return Response(
                {"error": "Exam already submitted. Contact administrator."},
                status=status.HTTP_403_FORBIDDEN
            )

        if serializer.is_valid():
            user = serializer.validated_data

            # 🔹 Get or create login attempt record
            attempt, _ = LoginAttempt.objects.get_or_create(user=user)

            # 🔸 Check if the user exceeded login limit
            if attempt.attempts >= 8:
                return Response(
                    {"error": "Maximum login attempts exceeded. Contact administrator."},
                    status=status.HTTP_403_FORBIDDEN
                )

            # Increment login count
            attempt.increment()

            # 🔑 Create JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                "message": "Login successful",
                "username": user.username,
                "attempts_left": 5 - attempt.attempts,
                "access": access_token,
                "refresh": refresh_token
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, time, timedelta
from .models import ExamSession, Question, UserResponse, LoginAttempt
from .utils import generate_user_exam
from .serializers import QuestionSerializer
import pytz  # make sure pytz is installed

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, time
import pytz

from .models import ExamSession, Question, LoginAttempt
from .serializers import QuestionSerializer
from .utils import generate_user_exam



class ExamDataAPI(APIView):
    def get(self, request, rollno):
        try:
            user = User.objects.get(username=rollno)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        # Current time in IST
       

        # Get or create exam session
        session, created = ExamSession.objects.get_or_create(
            user=user,
            defaults={'end_time': exam_end}
        )
        if session.completed:
            return Response({"error": "Exam already submitted"}, status=403)

        # Only increment login attempt if session is newly created
        if created:
            login_record, _ = LoginAttempt.objects.get_or_create(user=user)
            if login_record.attempts >= 8:
                return Response({"error": "Login limit exceeded. Contact admin."}, status=403)
            login_record.increment()

        # Assign questions if new session
        if created or session.questions.count() == 0:
            selected_qs = generate_user_exam()
            session.questions.set(selected_qs)
            session.save()
            from .tasks import auto_submit_exam
            auto_submit_exam.apply_async((session.id,), eta=exam_end)

        # Timer (remaining seconds)
        timer = max(int((exam_end - now).total_seconds()), 0)

        # Serialize questions
        questions = session.questions.all()
        serializer = QuestionSerializer(questions, many=True, context={'session': session})

        return Response({
            "username": user.username,
            "timer": timer,
            "warnings": session.warnings,
            "penalties": session.total_penalties,
            "questions": serializer.data
        })

# views.py
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import ExamSession, Question, UserResponse
from .serializers import UserResponseUpdateSerializer

class UpdateQuestionAPI(APIView):
    def post(self, request, rollno, question_id):
        # Get user
        user = get_object_or_404(User, username=rollno)

        # Get exam session
        session = get_object_or_404(ExamSession, user=user)

        # Get question
        question = get_object_or_404(Question, id=question_id)

        # Get or create user response
        user_response, _ = UserResponse.objects.get_or_create(
            exam_session=session,
            question=question
        )

        # Validate input
        serializer = UserResponseUpdateSerializer(data=request.data)
        if serializer.is_valid():
            selected_answer = serializer.validated_data['selected_answer']
            warnings_count = serializer.validated_data['warnings_count']

            # Update answer
            user_response.selected_answer = selected_answer
            user_response.save()

            # Update session warnings
            session.warnings += warnings_count
            
            session.save()

            # Calculate penalty (0.5 marks for each warning after 5)
            penalty_score = max(0, (session.warnings - 5) * 0.5)
            session.total_penalties = penalty_score
            session.save()

            return Response({
                "message": "Answer updated successfully",
                "question_id": question.id,
                "selected_answer": user_response.selected_answer,
                "is_correct": user_response.is_correct(),
                "penalty_score": penalty_score,
                "total_warnings": session.warnings
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import ExamSession, UserResponse

class FinalSubmitAPI(APIView):
    def post(self, request, rollno):
        # Get user and session
        user = get_object_or_404(User, username=rollno)
        session = get_object_or_404(ExamSession, user=user)
        if now < submission_start:
            return Response({"error": "Exam can only be submitted at 6:45 AM IST on 17th Oct 2025."}, status=403)

        # End the session
        session.end_time = timezone.now()
        session.completed = True
        session.save()

        # Get all user responses for this session
        responses = UserResponse.objects.filter(exam_session=session)

        # Calculate total marks
        total_marks = 0
        for resp in responses:
            if resp.is_correct():
                total_marks += resp.question.marks

        # Calculate penalty (0.5 per warning after 5)
        penalty = max(0, (session.warnings - 5) * 0.5)
        final_score = max(0, total_marks - penalty)

        # Prepare summary
        summary = []
        for resp in responses:
            summary.append({
                "question_id": resp.question.id,
                "selected_answer": resp.selected_answer,
                "correct_answer": resp.question.correct_answer,
                "is_correct": resp.is_correct(),
                "marks": resp.question.marks
            })

        return Response({
            "message": "Exam submitted successfully",
            "username": user.username,
            "total_questions": responses.count(),
            "total_marks": total_marks,
            "warnings": session.warnings,
            "penalty_score": penalty,
            "final_score": final_score,
            "responses": summary
        })
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FeedbackSerializer

class FeedbackAPI(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Feedback submitted successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.utils import timezone
from .models import ExamSession

class EndExpiredExamsAPI(APIView):
    permission_classes = [IsAdminUser]  # Only admins can call this

    def post(self, request):
        now = timezone.now()
        # Filter sessions whose end_time has passed and are not submitted
        expired_sessions = ExamSession.objects.filter(completed=False)

        count = 0
        for session in expired_sessions:
            session.completed = True
            # Optional: calculate final penalties, warnings, scores here
            session.save()
            count += 1

        return Response({
            "message": f"{count} exam session(s) successfully ended."
        })
