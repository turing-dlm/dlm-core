from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from dlm.views import login_redirect

urlpatterns = [
    path('', TemplateView.as_view(template_name='dlm/index.html')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('login-redirect/', login_redirect),
]
