from django.urls import path,include
from accounts import views
from django.contrib.auth import views as auth_view



app_name = 'accounts'

urlpatterns = [
    path('profile_update/',views.update_profile,name = 'profile_update'),
    path('register/',views.register,name = 'register'),
    path('login/',auth_view.LoginView.as_view(template_name = 'accounts/login.html'),name = 'login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('thanks/',views.ThanksView.as_view(),name = 'thanks')
]


