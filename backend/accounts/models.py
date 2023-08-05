from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class EmployeeManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_employee=True)

class HRManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_hr=True)

class AdminManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)

class NormalUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_employee=False, is_hr=False, is_admin=False, is_supportstaff=False)



class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Admin(User):
    objects = AdminManager()

    class Meta:
        proxy = True
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def save(self, *args, **kwargs):
        self.is_admin = True
        self.is_hr = False
        self.is_employee = False
        
        super().save(*args, **kwargs)


class HR(User):
    objects = HRManager()

    class Meta:
        proxy = True
        verbose_name = 'HR'
        verbose_name_plural = 'HRs'

    def save(self, *args, **kwargs):
        self.is_admin = False
        self.is_hr = True
        self.is_employee = True
        
        super().save(*args, **kwargs)


class Employee(User):
    objects = EmployeeManager()

    class Meta:
        proxy = True
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def save(self, *args, **kwargs):
        self.is_admin = False
        self.is_hr = False
        self.is_employee = True
        
        super().save(*args, **kwargs)

class NormalUser(User):
    objects = NormalUserManager()

    class Meta:
        proxy = True
        verbose_name = 'Normal User'
        verbose_name_plural = 'Normal Users'

    def save(self, *args, **kwargs):
        self.is_admin = False
        self.is_hr = False
        self.is_employee = False
        
        super().save(*args, **kwargs)
