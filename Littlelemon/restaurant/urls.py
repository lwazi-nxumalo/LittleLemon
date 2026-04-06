from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet, basename='bookings-api')

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu_page, name='menu'),
    path('menu/<int:pk>/', views.SingleMenuView.as_view()),
    path('reservations/', views.bookings, name='bookings'),
    path('api/', include(router.urls)),
    path('api/menu/', views.MenuItemView.as_view(), name='menu-api'),
    path('api/menu/<int:pk>/', views.SingleMenuView.as_view()),
]