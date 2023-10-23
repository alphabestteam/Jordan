from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404

class BookCreateView(View):
    @csrf_exempt
    def post(self, request):
        serializer = BookSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)

class BookUpdateView(View):
    @csrf_exempt
    def put(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

class BookDeleteView(View):
    @csrf_exempt
    def delete(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully'}, status=200)

@csrf_exempt
def list_books_by_genre(request):
    genre_filter = request.GET.get('genre') 
    if not genre_filter:
        return JsonResponse({'error': 'Genre parameter is required.'}, status=400)
    books = Book.objects.filter(genre=genre_filter)
    book_data = [{'title': book.title, 'author': book.author, 'genre': book.genre} for book in books]
    return JsonResponse(book_data, safe=False)

@csrf_exempt
def search_books_by_title(request):
    title_query = request.GET.get('title') 
    if not title_query:
        return JsonResponse({'error': 'Title parameter is required.'}, status=400)
    books = Book.objects.filter(title__icontains=title_query)
    book_data = [{'title': book.title, 'author': book.author, 'genre': book.genre} for book in books]
    return JsonResponse(book_data, safe=False)
