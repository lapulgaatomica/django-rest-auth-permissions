from django.urls import path
from .views import PagesAPIView

urlpatterns = [
    path('', PagesAPIView.as_view()),
]