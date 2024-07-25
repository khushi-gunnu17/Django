from django.urls import path
from . import views

# localhost:8000/django_app
# localhost:8000/django_app/fruit_stores/

urlpatterns = [
    path('', views.all_app, name='all_app'),
    path('<int:fruit_id>/', views.fruit_detail, name='fruit_detail'),
    path('fruit_stores/', views.fruit_stores, name='fruit_stores')
]
