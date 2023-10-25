from rest_framework.decorators import api_view
from django.views import APIView
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class BookCreateView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookDetailView(APIView):
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk= id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class BookUpdateView(APIView):
    def put(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class BookDeleteView(APIView):
    def delete(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return Response(serializer.data, status=status.HTTP_201_DELETED)
      
@api_view(['GET'])
def list_books_by_genre(request):
    genre_filter = request.GET.get('genre')
    if not genre_filter:
        return Response({'error': 'Genre parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

    books = Book.objects.filter(genre=genre_filter)
    serializer = BookSerializer(books, many=True) 
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def search_books_by_title(request):
    title_query = request.GET.get('title')
    if not title_query:
        return Response({'error': 'Title parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)










