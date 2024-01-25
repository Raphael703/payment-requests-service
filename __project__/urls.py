from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from users.views import UserLoginView, UserLogoutView, UserCreateView, UsersListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('sign-up/', UserCreateView.as_view(), name='sign_up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('users/', UsersListView.as_view(), name='users_list'),
    path('payment_requests/', include('payment_requests.urls'))
]
