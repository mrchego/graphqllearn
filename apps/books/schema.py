import graphene
# Imports GraphQL framework for Python.
from graphene_django import DjangoObjectType
# Bridge between:

# Django models
# GraphQL types

# Without this:
# you manually map fields yourself.
from apps.books.models import Book
# Imports Django model.

# Needed because GraphQL type is built FROM model.

class BookType(DjangoObjectType):
#     This converts Django model → GraphQL type.

# Internally

# Graphene inspects model:

# Book

# and auto-generates:

# type BookType {
#     id: ID
#     title: String
#     excerpt: String
# }

# Very important.

# This is AUTOMATIC schema generation.
    class Meta:
#         Configuration class.

# Used by Graphene internally.

# model = Book

# Tells Graphene:

# “Use Django Book model.”
        model = Book
#         Tells Graphene:

# “Use Django Book model.”
        fields = ("id", "title", "excerpt")
#         Controls exposed API fields.

# VERY important for:

# security
# performance
# API design

# Without this:
# you may accidentally expose sensitive data.

class Query(graphene.ObjectType):
#     Defines GraphQL queries clients can run.

# Think:

# “Available API operations.”
    all_books = graphene.List(BookType)
#     Creates GraphQL endpoint:

# allBooks

# Returning:

# list of books

# Internal Meaning

# Graphene creates schema:

# allBooks: [BookType]

# Meaning:

# array of BookType objects

    def resolve_all_books(root, info): # pylint: disable=no-self-argument
        """Return all books."""
#         MOST IMPORTANT CONCEPT.

# Resolvers fetch actual data.

# Think Of Resolver As
# GraphQL field
#       ↓
# Resolver runs
#       ↓
# Gets data
#       ↓
# Returns result

# Resolvers are basically:

# data-fetching functions
        return Book.objects.all()
#     Django ORM query.

# Internally generates SQL:

# SELECT * FROM books;

schema = graphene.Schema(query=Query)
# Creates entire GraphQL schema.

# This becomes:

# API contract
# query engine
# validation system

