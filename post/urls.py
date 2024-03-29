from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('who/<int:pk>', views.DetailView.as_view(), name='detail'),
]