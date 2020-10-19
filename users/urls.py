from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
	url(r'^login', LoginView.as_view(template_name='users/login.html'), name='login'),
	url(r'^logout', views.logout_view, name='logout'),
	url(r'^register/', views.register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        views.activate, name='activate'),
]
