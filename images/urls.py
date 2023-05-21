from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    # path('edit/<int:id>/<slug:slug>/', views.edit_images, name='edit'),
    path('like/', views.image_like, name='like'),
    path('', views.image_list, name='list'),
]
