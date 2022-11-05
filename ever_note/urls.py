from django.urls import path
from ever_note import views

urlpatterns = [
    path('create/', views.create_test_note, name='create_note')
]