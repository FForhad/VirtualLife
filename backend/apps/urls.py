from django.urls import path, include

# from apps.core.views import download_view

urlpatterns = [
    # path('homes/', include('apps.homes.urls'), name='users'),
    path('users/', include('apps.users.urls'), name='users'),
    # path('auth/', include('apps.auths.urls'), name='auths'),
    # path('', include('apps.externals.urls'), name='externals'),
]