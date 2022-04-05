from django.contrib import admin
from home.models import Contact

# Register your models here.
admin.site.register(Contact)

# after this, register your app by copying the app name and pasting it in settings.py
