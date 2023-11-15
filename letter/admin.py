from django.contrib import admin
from .models import Letter

class LetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'letter_id', 'user', 'created_at' )
admin.site.register(Letter, LetterAdmin)