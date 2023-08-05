from django.db import models
from profiles.models import Profile
from accounts.models import Employee

#####branches


class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name='Department Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Job(models.Model):
    name = models.CharField(max_length=150, verbose_name='Job Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    grade = models.CharField(max_length=150, blank=True, null=True, verbose_name='Grade')
    salary_range = models.CharField(max_length=150, blank=True, null=True, verbose_name='Salary Range')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Department')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class Employee(models.Model):
    user = models.OneToOneField(Employee, on_delete=models.CASCADE)
    job_title = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name='Job Title')

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class Recruitment(models.Model):
    position = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name='Job Position')
    available_slots = models.SmallIntegerField(default=1, verbose_name='Available Slots')
    created = models.DateTimeField(verbose_name='Created')
    deadline = models.DateTimeField(verbose_name='Deadline')
    updated = models.DateField(verbose_name='Updated')

    class Meta:
        verbose_name = 'Recruitment'
        verbose_name_plural = 'Recruitments'


class Training(models.Model):
    title = models.CharField(max_length=100, verbose_name='Training Title')
    description = models.TextField(verbose_name='Description')
    # Other training fields

    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'


class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Employee')
    date = models.DateField(verbose_name='Date')
    rating = models.PositiveIntegerField(verbose_name='Rating')
    # Other performance fields

    class Meta:
        verbose_name = 'Performance'
        verbose_name_plural = 'Performances'


class Leave(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('on_leave', 'On Leave')
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Employee')
    reason=models.TextField()
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Status')
    # Other leave fields

    class Meta:
        verbose_name = 'Leave'
        verbose_name_plural = 'Leaves'


class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Employee')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    period = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Period')

    # Other payroll fields

    class Meta:
        verbose_name = 'Payroll'
        verbose_name_plural = 'Payrolls'


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Employee')
    date = models.DateField(verbose_name='Date')
    time_in = models.TimeField(verbose_name='Time In')
    time_out = models.TimeField(verbose_name='Time Out')
    updated = models.DateField(verbose_name='Updated')

    # Other attendance fields

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendance'
