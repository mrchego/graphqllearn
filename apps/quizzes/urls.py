from django.urls import path
from graphene_django.views import GraphQLView
from  apps.quizzes.schema import  schema


app_name = "quizzes"

urlpatterns = [
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema))
]

