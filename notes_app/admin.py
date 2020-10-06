from django.contrib import admin
from notes_app.models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)