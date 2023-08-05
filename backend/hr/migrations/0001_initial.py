# Generated by Django 4.1.7 on 2023-06-18 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_delete_supportstaff_remove_user_is_supportstaff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Department Name')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Job Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('grade', models.CharField(blank=True, max_length=150, null=True, verbose_name='Grade')),
                ('salary_range', models.CharField(blank=True, max_length=150, null=True, verbose_name='Salary Range')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.department', verbose_name='Department')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Training Title')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Training',
                'verbose_name_plural': 'Trainings',
            },
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_slots', models.SmallIntegerField(default=1, verbose_name='Available Slots')),
                ('created', models.DateTimeField(verbose_name='Created')),
                ('deadline', models.DateTimeField(verbose_name='Deadline')),
                ('updated', models.DateField(verbose_name='Updated')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.job', verbose_name='Job Position')),
            ],
            options={
                'verbose_name': 'Recruitment',
                'verbose_name_plural': 'Recruitments',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('rating', models.PositiveIntegerField(verbose_name='Rating')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Performance',
                'verbose_name_plural': 'Performances',
            },
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('period', models.DateField(verbose_name='Period')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Payroll',
                'verbose_name_plural': 'Payrolls',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('on_leave', 'On Leave')], max_length=20, verbose_name='Status')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Leave',
                'verbose_name_plural': 'Leaves',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.job', verbose_name='Job Title'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('time_in', models.TimeField(verbose_name='Time In')),
                ('time_out', models.TimeField(verbose_name='Time Out')),
                ('updated', models.DateField(verbose_name='Updated')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendance',
            },
        ),
    ]