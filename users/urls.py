from django.urls import path

from users.views import UserLoginView, UserLogoutView, UserCreateView, UsersListView

urlpatterns = [
    path('', UsersListView.as_view(), name='users_list'),
    path('sign-up/', UserCreateView.as_view(), name='sign_up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
