from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.utils.translation import gettext_lazy as _

from users.forms import CustomUserCreationForm
from users.mixins import AdminRequiredMixin


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    success_message = _('Аккаунт успешно создан')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('index')
    success_message = _('Вы успешно авторизовались')


class UserLogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('Вы вышли из системы'))
        return super().dispatch(request, *args, **kwargs)


class UsersListView(AdminRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'users/list.html'
    context_object_name = 'users'

    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_users_amount'] = self.model.objects.all().count()
        return context
