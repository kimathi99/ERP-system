from django.contrib import admin
from .models import Attendance,Payroll,Leave,Job,Department 
# Register your models here.


admin.site.register(Attendance)
admin.site.register(Leave)
admin.site.register(Department)
admin.site.register(Payroll)