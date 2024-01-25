from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, _('Только администраторы могут просматривать данную страницу'))
        return redirect('index')


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request, _('Данную страницу могут просматривать '
                                       'только авторизованные пользователи'))
        return redirect(settings.LOGIN_URL)
