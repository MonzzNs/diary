from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .models import Diary 
from django.contrib.auth import get_user_model
# Register your models here.

User = get_user_model()

class AdminDisplay(UserAdmin):
    fields = ('username','full_name','is_staff', 'is_superuser', 'is_active')
    list_display = ('username','full_name','is_staff', 'is_superuser', 'is_active')
    search_fields = ('username','full_name')
    readonly_fields = ['last_login']
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User,AdminDisplay)

class DiaryDisplay(admin.ModelAdmin):
    fields = ('user', 'title', 'diary', 'img', 'slug', 'date')
    list_display = ('user', 'title', 'diary', 'date', 'slug')
    search_fields = ('user__username', 'title')
    readonly_fields = ['date']
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Diary, DiaryDisplay)