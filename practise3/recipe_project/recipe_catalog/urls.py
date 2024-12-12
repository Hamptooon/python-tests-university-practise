from django.urls import path
from .views import about, index, recipe_detail, register, user_login, user_logout
urlpatterns = [
	path('', index, name='index'),
	path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
	path('about/', about, name='about'),
	path('register/', register, name='register'),
	path('login/', user_login, name='login'),
	path('logout/', user_logout, name='logout'),
]