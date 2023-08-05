from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Admin, HR, Employee,  NormalUser


class CustomUserAdmin(UserAdmin):
    list_filter=('is_staff','is_active')
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password'),
            'classes': ('wide',),
        }),
        ('Personal Details', {
            'fields': ('first_name', 'last_name'),
            'classes': ('collapse',),
        }),
        ('Group Section', {
            'fields': ('groups',),
            'classes': ('collapse',),
        }),
        ('Job Type', {
            'fields': ('is_admin', 'is_hr', 'is_employee'),
            'classes': ('collapse',),
        }),
        ('permisions', {
            'fields': ( 'is_staff', 'is_active'),
            'classes': ('collapse',),
        }),
    )


class AdminAdmin(CustomUserAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password'),
            'classes': ('wide',),
        }),
        ('Personal Details', {
            'fields': ('first_name', 'last_name'),
            'classes': ('collapse',),
        }),
        ('Group Section', {
            'fields': ('groups',),
            'classes': ('collapse',),
        }),
        
    )


class HRAdmin(CustomUserAdmin):
   fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password'),
            'classes': ('wide',),
        }),
        ('Personal Details', {
            'fields': ('first_name', 'last_name'),
            'classes': ('collapse',),
        }),
        ('Group Section', {
            'fields': ('groups',),
            'classes': ('collapse',),
        }),
        
    )


class EmployeeAdmin(CustomUserAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password'),
            'classes': ('wide',),
        }),
        ('Personal Details', {
            'fields': ('first_name', 'last_name'),
            'classes': ('collapse',),
        }),
        ('Group Section', {
            'fields': ('groups',),
            'classes': ('collapse',),
        }),
        
    )



class NormalUserAdmin(CustomUserAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password'),
            'classes': ('wide',),
        }),
        ('Personal Details', {
            'fields': ('first_name', 'last_name'),
            'classes': ('collapse',),
        }),
        ('Group Section', {
            'fields': ('groups',),
            'classes': ('collapse',),
        }),
        
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(HR, HRAdmin)
admin.site.register(NormalUser, NormalUserAdmin)
admin.site.register(Employee, EmployeeAdmin)

