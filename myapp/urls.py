from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),  # View all items
    path('add/', views.add_item, name='add_item'),  # Add an item
    path('edit/<int:pk>/', views.edit_item, name='edit_item'),  # Edit item
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),  # Delete item
]
