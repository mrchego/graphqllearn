from pyexpat import model

import graphene
from graphene_django import DjangoObjectType, DjangoListField
from apps.quizzes.models import Category, Quiz, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = ("id", "title","category", "date_created")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = (
            "id",
            "quiz",
            "technique",
            "title",
            "difficulty",
            "date_created",
            "is_active",
        )


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id", "question", "answer_text", "is_right")

class  Query(graphene.ObjectType):
    # all_categories = graphene.List(CategoryType)
    # quiz = graphene.String()

    # def resolve_quiz(root, info):  # pylint: disable=no-self-argument
    #     return f"This is the first question"

    # all_quizzes = DjangoListField(QuizType)
    # all_quizzes = graphene.Field(QuizType, id=graphene.Int())
    # all_questions = DjangoListField(QuestionType)
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    # def resolve_all_quizzes(root, info, id):
    #     return Quiz.objects.get(pk=id)

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)

schema = graphene.Schema(query=Query)
