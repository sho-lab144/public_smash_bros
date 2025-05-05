from django.urls import path, include
from .views import match_list, create_match, delete_match, edit_match

app_name = 'matches'

urlpatterns = [
    path('', match_list, name='match_list'),
    path('create/', create_match, name='create_match'),
    path('<uuid:match_id>/delete/', delete_match, name='delete_match'),
    path('<uuid:match_id>/edit/', edit_match, name='edit_match'),
]