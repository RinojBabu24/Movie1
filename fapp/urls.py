from . import views
from django.contrib import admin
from django.urls import path
app_name='fapp'

urlpatterns = [
    path('',views.demo,name='demo'),
    path('demo1/',views.demo1,name='demo1'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

    ]