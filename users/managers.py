from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, full_name, is_staff=False, is_superuser=False, is_active=True):
        if not email:
            raise ValueError(_("Email is required"))
        if not password:
            raise ValueError(_("User must have a password"))
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.full_name = full_name
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.is_active = is_active
        user.save()
        return user
    
    def create_superuser(self, email, password, full_name):
        return self.create_user(email, password, full_name, is_staff=True, is_superuser=True)