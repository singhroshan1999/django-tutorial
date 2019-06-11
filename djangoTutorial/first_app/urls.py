#####
from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('relative_path',views.relative_path,name = 'relative_path2'),
]
