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


# --------------------------------ADD MUTATION -----------------------------
# class AddCategoryMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)

#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info, name):
#         category = Category(name=name)
#         category.save()
#         return CategoryMutation(category=category)

# class QuizMutation(graphene.Mutation):
#     class Arguments:
#         title = graphene.String()
#         category_id = graphene.ID()

#     quiz = graphene.Field(QuizType)
#     @classmethod
#     def mutate(cls, root, info, title, category_id):
#         category = Category.objects.get(id=category_id)
#         quiz = Quiz(title=title, category=category)
#         quiz.save()
#         return QuizMutation(quiz=quiz)
    

# mutation {
#   addQuiz(categoryId: 1, title:"django"){
#     quiz{
#       title
#       category{
#         name
#       }
#     }
#   }
# }

# --------------------------------UPDATE MUTATION -----------------------------
# class UpdateCategoryMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)
#         name = graphene.String(required=True)

#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info, name, id):
#         category = Category.objects.get(id=id)
#         category.name = name
#         category.save()
#         return CategoryMutation(category=category)

# class UpdateQuizMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)
#         category_id = graphene.ID(required=True)
#         title = graphene.String()

#     quiz = graphene.Field(QuizType)
#     @classmethod
#     def mutate(cls, root, info, id ,category_id, title):
#         quiz  = Quiz.objects.get(id=id)
#         category = Category.objects.get(id=category_id)
#         quiz.title = title
#         quiz.category = category
#         quiz.save()
#         return UpdateQuizMutation(quiz=quiz)

# mutation {
#   updateQuiz(id: 3,categoryId: 1, title:"django ninja"){
#     quiz{
#       title
#       category{
#         name
#       }
#     }
#   }
# }

# --------------------------------DELETE MUTATION -----------------------------
# class DeleteCategoryMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)

#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info, id):
#         category = Category.objects.get(id=id)
#         category.delete()
#         return

class DeleteQuizMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    quiz = graphene.Field(QuizType)

    @classmethod
    def mutate(cls, root, info, id):
        quiz = Quiz.objects.get(id=id)
        quiz.delete()
        return

# mutation {
#   deleteQuiz(id:3){
#     quiz{
#       title
#       category{
#         name
#       }
#     }
#   }
# }
class Mutation(graphene.ObjectType):
    # add_category = AddCategoryMutation.Field()
    # update_category = UpdateCategoryMutation.Field()
    # delete_category = DeleteMutation.Field()
    # add_quiz = QuizMutation.Field()
    # update_quiz = UpdateQuizMutation.Field()
    delete_quiz = DeleteQuizMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
