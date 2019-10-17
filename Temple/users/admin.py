from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm1, CustomUserChangeForm1
from .models import CustomUser1

# Register your models here.

class CustomUserAdmin1(UserAdmin):
    add_form = CustomUserCreationForm1
    form = CustomUserChangeForm1
    list_display = ['email', 'username','age']
    model = CustomUser1

admin.site.register(CustomUser1, CustomUserAdmin1)