from django.contrib import admin
from .models import user  
from .models import brand

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'dob')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    list_filter = ('dob',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name_kh', 'name_en', 'order', 'email')
    search_fields = ('name_kh', 'name_en', 'email')

admin.site.register(user, UserAdmin)
admin.site.register(brand, BrandAdmin)






 