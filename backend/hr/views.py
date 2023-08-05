from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import DepartmentForm, JobForm, RecruitmentForm, TrainingForm, PerformanceForm, LeaveForm, PayrollForm, AttendanceForm
from .models import Department, Job, Recruitment, Training, Performance, Leave, Payroll, Attendance

# POST and GET Views
class DepartmentView(View):
    def get(self, request):
        form = DepartmentForm()
        departments = Department.objects.all()
        return render(request, 'department.html', {'form': form, 'departments': departments})

    def post(self, request):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department')
        departments = Department.objects.all()
        return render(request, 'department.html', {'form': form, 'departments': departments})


class JobView(View):
    def get(self, request):
        form = JobForm()
        jobs = Job.objects.all()
        return render(request, 'job.html', {'form': form, 'jobs': jobs})

    def post(self, request):
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job')
        jobs = Job.objects.all()
        return render(request, 'job.html', {'form': form, 'jobs': jobs})


class RecruitmentView(View):
    def get(self, request):
        form = RecruitmentForm()
        recruitments = Recruitment.objects.all()
        return render(request, 'recruitment.html', {'form': form, 'recruitments': recruitments})

    def post(self, request):
        form = RecruitmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recruitment')
        recruitments = Recruitment.objects.all()
        return render(request, 'recruitment.html', {'form': form, 'recruitments': recruitments})


class TrainingView(View):
    def get(self, request):
        form = TrainingForm()
        trainings = Training.objects.all()
        return render(request, 'training.html', {'form': form, 'trainings': trainings})

    def post(self, request):
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training')
        trainings = Training.objects.all()
        return render(request, 'training.html', {'form': form, 'trainings': trainings})


class PerformanceView(View):
    def get(self, request):
        form = PerformanceForm()
        performances = Performance.objects.all()
        return render(request, 'performance.html', {'form': form, 'performances': performances})

    def post(self, request):
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance')
        performances = Performance.objects.all()
        return render(request, 'performance.html', {'form': form, 'performances': performances})


class LeaveView(View):
    def get(self, request):
        form = LeaveForm()
        leaves = Leave.objects.all()
        return render(request, 'leave.html', {'form': form, 'leaves': leaves})

    def post(self, request):
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave')
        leaves = Leave.objects.all()
        return render(request, 'leave.html', {'form': form, 'leaves': leaves})


class PayrollView(View):
    def get(self, request):
        form = PayrollForm()
        payrolls = Payroll.objects.all()
        return render(request, 'payroll.html', {'form': form, 'payrolls': payrolls})

    def post(self, request):
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll')
        payrolls = Payroll.objects.all()
        return render(request, 'payroll.html', {'form': form, 'payrolls': payrolls})


class AttendanceView(View):
    def get(self, request):
        form = AttendanceForm()
        attendances = Attendance.objects.all()
        return render(request, 'attendance.html', {'form': form, 'attendances': attendances})

    def post(self, request):
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance')
        attendances = Attendance.objects.all()
        return render(request, 'attendance.html', {'form': form, 'attendances': attendances})


# Detail Views
class DepartmentDetailView(View):
    def get(self, request, department_id):
        department = get_object_or_404(Department, id=department_id)
        return render(request, 'department_detail.html', {'department': department})


class JobDetailView(View):
    def get(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        return render(request, 'job_detail.html', {'job': job})


class RecruitmentDetailView(View):
    def get(self, request, recruitment_id):
        recruitment = get_object_or_404(Recruitment, id=recruitment_id)
        return render(request, 'recruitment_detail.html', {'recruitment': recruitment})

# Create similar detail views for the remaining models
