from users.views import user_login, log_out, user_signup, home
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', log_out, name="logout"),
    path('', home, name="home")
]