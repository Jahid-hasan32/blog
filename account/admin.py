from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):

    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "usename", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('details', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["usename"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            'new user',
            {
                "classes": ["wide"],
                "fields": ["email", "usename", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

admin.site.register(User, UserAdmin)
