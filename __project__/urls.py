from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from __project__.yasg import urlpatterns as yasg_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('users/', include('users.urls')),
    path('payment-requests/', include('payment_requests.urls'))
]
urlpatterns += yasg_urlpatterns
