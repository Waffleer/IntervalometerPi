from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Setting)
admin.site.register(Cycle)
admin.site.register(Type)
admin.site.register(Run)