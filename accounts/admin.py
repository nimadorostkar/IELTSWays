from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'first_name', 'last_name', 'withdraw', 'created_at')
    list_filter = ("created_at", "withdraw")
    search_fields = ['national_id', 'first_name', 'last_name']
    readonly_fields = ('created_at',)
admin.site.register(User, UserAdmin)

