from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Article
from .permissions import IsAuthorSuperUserorReadOnly
from .serializers import ArticleSerializer


class PagesAPIViewList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PageAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorSuperUserorReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
