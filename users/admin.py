from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['email','full_name']
    ordering = ('email',)
    fieldsets = (
                    (None,{'fields':('email','password')}),
                    ('Personal Details',{'fields':('full_name',)}),
                    ('Permissions',{'fields':('is_staff','is_superuser','is_active')})
                )
    add_fieldsets = (
                    (None,{'classes':('wide',),'fields':('email','password1','password2','full_name','is_staff','is_superuser','is_active')}),
                )