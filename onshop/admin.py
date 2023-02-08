from django.contrib import admin
from .models import Product, Rubric, Comments

admin.site.register(Product)
admin.site.register(Rubric)
admin.site.register(Comments)