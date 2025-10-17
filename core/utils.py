import random
from .models import Question

def generate_user_exam():
    # Get all 1-mark and 2-mark questions
    one_mark_qs = list(Question.objects.filter(marks=1))
    two_mark_qs = list(Question.objects.filter(marks=2))

    # Check if there are enough questions
    if len(one_mark_qs) < 20:
        raise ValueError("Not enough 1-mark questions in the database to generate exam.")
    if len(two_mark_qs) < 20:
        raise ValueError("Not enough 2-mark questions in the database to generate exam.")

    # Pick random questions
    selected_one_mark = random.sample(one_mark_qs, 20)
    selected_two_mark = random.sample(two_mark_qs, 20)

    # Combine and shuffle
    selected_questions = selected_one_mark + selected_two_mark
    random.shuffle(selected_questions)

    return selected_questions
