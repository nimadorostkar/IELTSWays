from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'first_name', 'last_name', 'created_at')
    search_fields = ['national_id', 'first_name', 'last_name']
admin.site.register(User, UserAdmin)

