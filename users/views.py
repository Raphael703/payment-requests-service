from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from users.forms import CustomUserCreationForm


class UserCreateView(CreateView):
    template_name = 'users/create.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('index')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class UsersListView(ListView):
    model = get_user_model()
    template_name = 'users/list.html'
    context_object_name = 'users'

    paginate_by = 16
