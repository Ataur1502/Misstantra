# serializers.py
from rest_framework import serializers
from .models import UserResponse

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ['exam_session', 'question', 'selected_answer', 'is_penalized']

# serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
    

from rest_framework import serializers
from .models import ExamSession

class StartExamSerializer(serializers.Serializer):
    exam_id = serializers.IntegerField()


from rest_framework import serializers
from .models import Question, UserResponse

class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    user_answer = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField() 

    class Meta:
        model = Question
        fields = ['id', 'text', 'options', 'user_answer','image_url']

    def get_options(self, obj):
        return {
            "A": obj.option_a,
            "B": obj.option_b,
            "C": obj.option_c,
            "D": obj.option_d
        }

    def get_user_answer(self, obj):
        session = self.context.get('session')
        if not session:
            return None
        response = UserResponse.objects.filter(exam_session=session, question=obj).first()
        return response.selected_answer if response else None
    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url  # Django builds static URL automatically
        return None
# serializers.py
# serializers.py
from rest_framework import serializers
from .models import UserResponse

class UserResponseUpdateSerializer(serializers.Serializer):
    selected_answer = serializers.ChoiceField(choices=['A','B','C','D','N'])
    warnings_count = serializers.IntegerField(min_value=0)

    def validate(self, data):
        if 'selected_answer' not in data:
            raise serializers.ValidationError("selected_answer is required")
        if 'warnings_count' not in data:
            raise serializers.ValidationError("warnings_count is required")
        return data
# serializers.py
from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'rating', 'feedback_text', 'submitted_at']
