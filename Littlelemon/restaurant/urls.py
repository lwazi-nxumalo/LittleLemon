from django.urls import path
from .views import index, MenuItemView, SingleMenuView

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', SingleMenuView.as_view()),
]
