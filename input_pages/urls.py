from django.urls import path
from . import views

APP_NAME = 'input_pages'

urlpatterns = [
    path('', views.index, name='index'), # Home page
    path('saved-text/', views.saved_text, name='saved_text') # Data-displaying page
]
