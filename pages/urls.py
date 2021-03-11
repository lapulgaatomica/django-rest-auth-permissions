from django.urls import path
from .views import PagesAPIViewList, PageAPIViewDetail

urlpatterns = [
    path('', PagesAPIViewList.as_view()),
    path('<int:pk>/', PageAPIViewDetail.as_view()),
]