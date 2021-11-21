from django.urls import path
from . import views


app_name = 'showcase'
urlpatterns = [
    path('', views.index, name='index'),
    path('item/<slug:slug>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.ddformview, name='create'),
]


