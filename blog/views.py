from rest_framework import generics, filters, viewsets
from .serializer import AuthorSerializer, CategorySerializer, ArticleSerializer, CommentSerializer, ImageSerializer
from .models import Author, Category, Article, Comment, Image

from rest_framework import generics
from haystack.query import SearchQuerySet
from .models import Article


class ArticleSearchList(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        search_results = SearchQuerySet().models(Article).filter(content=query)
        article_ids = [result.object.id for result in search_results]
        queryset = Article.objects.filter(id__in=article_ids)
        return queryset


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Fields to search for

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class AuthorDetail(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
