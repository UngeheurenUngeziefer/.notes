from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include(('notes_app.urls', 'notes_app'), namespace='notes_app')),
]
