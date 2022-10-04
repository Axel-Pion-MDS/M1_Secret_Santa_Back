from django.contrib import admin

from .models import Santa, SantaMember

# Register your models here.
admin.site.register(Santa)
admin.site.register(SantaMember)
