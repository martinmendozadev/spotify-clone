"""User models admin."""

# Django
from django.contrib import admin

# Models
from spotify.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_verified',)
    search_fields = ('email', 'username')
    list_filter = ('is_verified', 'created', 'modified')

    readonly_fields = ('username', 'created', 'modified')
