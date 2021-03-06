from pages.views import handler404, handler500
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls'), name='pages'),
    path('users/', include('users.urls'), name='users'),
    path('vaccine/', include('vaccine.urls'), name='vaccine'),
    path('accounts/', include('allauth.urls'), name='accounts'),
    path('admin/', admin.site.urls, name='admin'),
]

handler404 = 'pages.views.handler404'
handler500 = 'pages.views.handler500'
