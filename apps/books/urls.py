from django.urls import path
# Used to define URL routes.

# Without this:
# Django cannot map URLs.
from graphene_django.views import GraphQLView
# VERY important.

# This is the actual GraphQL HTTP handler.

# Think of it as:

# "GraphQL request processor"

# It:

# receives requests
# parses GraphQL queries
# validates schema
# executes resolvers
# serializes responses

# This is basically the GraphQL engine entry point.
from apps.books.schema import schema
# Imports your GraphQL schema.

# Remember:

# Schema = blueprint of entire GraphQL API

# Contains:

# queries
# mutations
# types
# resolvers

# Without schema:
# GraphQLView knows NOTHING about your API.
app_name = "books"
# Used for URL namespacing.

# Lets Django reference routes safely.

# Example:

# books:graphql

# instead of ambiguous names.

# Important in large apps.
urlpatterns = [
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
# urlpatterns = [

# List of routes for this app.

# Django scans this to match URLs.

# 6. GraphQL Route
# path("graphql/", ...)

# Creates endpoint:

# /books/graphql/

# This becomes your API endpoint.

# 7. THE MOST IMPORTANT LINE
# GraphQLView.as_view(graphiql=True, schema=schema)

# This is where EVERYTHING happens.

# 8. WHAT IS as_view()?

# GraphQLView is a CLASS-BASED VIEW.

# Django views can be:

# function-based
# class-based

# as_view() converts class → callable Django view function.

# INTERNAL FLOW
# GraphQLView Class
#         ↓
# as_view()
#         ↓
# Creates View Instance
#         ↓
# Returns Callable Function
#         ↓
# Django Can Execute It

# Without as_view()
# Django cannot use class as route handler.

# 9. WHAT IS graphiql=True?

# Enables GraphiQL interface.

# VERY important for development.

# WHAT IS GRAPHIQL?

# Interactive GraphQL playground in browser.

# Like Postman built into GraphQL.

# Lets developers:

# write queries
# test APIs
# inspect schema
# debug resolvers
# Example

# Visit:

# /books/graphql/

# You get UI where you can run:

# {
#   allBooks {
#     title
#   }
# }

# and instantly see results.

# Why Important

# Without GraphiQL:
# testing GraphQL is painful.

# With it:
# development becomes MUCH faster.

# SECURITY NOTE

# Senior engineers usually disable GraphiQL in production.

# Why?

# Because:

# exposes API structure
# helps attackers inspect schema

# Usually:

# graphiql=settings.DEBUG

# instead of always True.

# 10. schema=schema
# schema=schema

# Passes GraphQL schema into engine.

# This tells GraphQLView:

# "Here are the available queries,
# types, and resolvers."
