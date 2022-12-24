from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('adding/', views.create_item, name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    # path('api/items/', views.get_items, name='get_items'),
    path('api/items/', views.GetItemsAPIView.as_view(), name='get_items'),
    path('api/items/create/', views.CreateItemAPIView.as_view(), name='create_item'),
    path('api/items/<int:id>/', views.ItemAPIView.as_view(), name='get_item'),
    path('api/items/<int:id>/update/', views.UpdateItemAPIView.as_view(), name='update_item'),
    path('api/items/<int:id>/delete/', views.DeleteItemAPIView.as_view(), name='delete_item'),
]


urlpatterns = format_suffix_patterns(urlpatterns)