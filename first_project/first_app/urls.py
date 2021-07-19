from django.urls import path
from first_app import views

app_name = 'first_app'
urlpatterns = [

    path('register/',views.register_view,name="register"),
    path('user_login/',views.user_login,name="user_login"),
]
