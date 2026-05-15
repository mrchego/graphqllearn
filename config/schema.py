import graphene
import graphql_auth
import graphql_jwt

from apps.books.schema import Query as BooksQuery
from apps.quizzes.schema import Mutation as QuizzesMutation
from apps.quizzes.schema import Query as QuizzesQuery

class Query(
    BooksQuery,
    QuizzesQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    QuizzesMutation,
    graphene.ObjectType,
    ):
    # GraphQL Auth
    # register = graphql_auth.Register.Field()
    # verify_account = graphql_auth.VerifyAccount.Field()

    # Login / JWT
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

    # Password reset
    # password_reset = graphql_auth.PasswordReset.Field()
    # password_change = graphql_auth.PasswordChange.Field()

    # Email changes
    # update_account = graphql_auth.UpdateAccount.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
