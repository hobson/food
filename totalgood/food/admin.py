from django.contrib import admin
from django.db.models import get_app, get_models
from .models import Nutrient

#admin.site.register(Nutrient)

app = get_app('food')

for model in get_models(app):
    admin.site.register(model)