from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Article
from .permissions import IsAuthorOrSuperUser
from .serializers import ArticleSerializer


class PagesAPIViewList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class PagesAPIViewDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthorOrSuperUser]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
