from django.contrib import admin
from .models import user  
from .models import brands
from .models import type

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'dob')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    list_filter = ('dob',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name_kh', 'name_en', 'order', 'is_active')
    search_fields = ('name_kh', 'name_en')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name',)

admin.site.register(user, UserAdmin)
admin.site.register(brands, BrandAdmin)
admin.site.register(type, TypeAdmin)





 