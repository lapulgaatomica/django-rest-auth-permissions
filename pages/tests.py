from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Article


class ArticleTests(APITestCase):
    def test_create_article(self):
        user = User.objects.create_user('lauren', 'secret')
        self.client.force_authenticate(user=user)
        data = {'paragraph': 'test article', 'author': 1}
        response = self.client.post('/api/v1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
