#####
from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('relative_path',views.relative_path,name = 'relative_path2'),
    path('register',views.register,name = 'register'),
    path('login',views.user_login,name = 'login'),
    path('logout',views.user_logout,name = 'logout'),
    path('special',views.only_login_user_can_see,name = 'special'),
]
