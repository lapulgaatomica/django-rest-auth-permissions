from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Article
from .serializers import ArticleSerializer


class ArticleTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user('lauren', 'secret')
        self.client.force_authenticate(user=user)
        data = {'paragraph': 'test article', 'author': 1}
        self.post_response = self.client.post('/api/v1/', data, format='json')
        self.read_response = self.client.get('/api/v1/1/')
        response_article = Article.objects.get(id=1)
        self.serializedArticle = ArticleSerializer(response_article)

    def test_create_article(self):
        self.assertEqual(self.post_response.status_code, status.HTTP_201_CREATED)

    def test_read_article(self):
        self.assertEqual(self.read_response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.read_response.data, self.serializedArticle.data)
