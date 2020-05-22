from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add/', views.post_add, name='post_add'),
    path('memo/<int:pk>', views.post_detail, name='post_detail'),
    path('memo/<int:pk>/update/', views.post_update, name='post_update'),
    path('memo/<int:pk>/delete', views.post_delete, name='post_delete')
]
