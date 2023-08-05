from django import forms
from .models import Department, Job, Recruitment, Training, Performance, Leave, Payroll, Attendance

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = '__all__'

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = '__all__'

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
