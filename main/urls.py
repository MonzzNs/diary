from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login_page, name='login'),
    path('home/', views.home, name='home'),
    path('logout', views.user_logout, name='logout'),
    path('delete-confirmation', views.del_confirmation, name='del_confir'),
    path('logout-confirmation', views.logout_confirmation, name='logout_confir'),
    path('create-diary', views.create_diary, name='create'),
    re_path('delete/(?P<slug>[-a-zA-Z0-9]+)/$', views.delete, name='delete'),
    re_path('view/(?P<slug>[-a-zA-Z0-9]+)/$', views.view_diary, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


