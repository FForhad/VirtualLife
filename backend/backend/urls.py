
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from apps.users.views.social_auth import GoogleLoginAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls'), name='api'),
    path('auth/google-login/', GoogleLoginAPIView.as_view(), name='google-login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]


