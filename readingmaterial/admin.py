from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Story)
admin.site.register(Tag)