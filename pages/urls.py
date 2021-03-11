from django.urls import path
from .views import PagesAPIViewList, PagesAPIViewDetail

urlpatterns = [
    path('', PagesAPIViewList.as_view()),
    path('<int:pk>/', PagesAPIViewDetail.as_view()),
]