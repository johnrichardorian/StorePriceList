from django.contrib import admin

# Register your models here.
from .models import Inventory
from .models import StoreProfile

admin.site.register(Inventory)
admin.site.register(StoreProfile)