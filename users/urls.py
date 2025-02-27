from django.urls import path

from users import views

app_name = "users" # имя приложения для маршрутизации

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("registration/", views.UserRegistrationView.as_view(), name="registration"),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
    path("users-basket/", views.UserBasketView.as_view(), name="users_basket"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
]
