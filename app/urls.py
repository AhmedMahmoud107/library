from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('books',views.books , name='books'),
    path('update/<int:id>',views.Update , name='update'),
    path('delete/<int:id>',views.Delete , name='delete'),

]