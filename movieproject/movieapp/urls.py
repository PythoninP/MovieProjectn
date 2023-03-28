from django.urls import path
from.import views

app_name = 'movieapp'
urlpatterns = [

    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movies, name='add'),
    path('update/<int:id>/', views.update, name='upd'),
    path('delete/<int:id>/', views.delete, name='dlt'),
    path('', views.submit, name='smt'),
]