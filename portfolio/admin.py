from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from .models import *
app_models = apps.get_app_config('portfolio').get_models()
# Register your models here.
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
