from .import views
from django.urls import path

app_name = 'films'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:film_id>/', views.details, name='detail'),
    path('add', views.new_film, name='new_film'),
    path('edit/<int:id>', views.edit_film, name='edit_film'),
    path('delete/<int:id>', views.delete_film, name='delete_film')
]
