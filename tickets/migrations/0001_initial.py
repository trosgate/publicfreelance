# Generated by Django 4.1.3 on 2023-02-20 11:04

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_settings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title field is Required', max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('description', ckeditor.fields.RichTextField(error_messages={'name': {'max_length': 'Description field is required'}}, max_length=3500, verbose_name='Description')),
                ('reference', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Ticket #')),
                ('status', models.CharField(choices=[('unassigned', 'Not Assigned'), ('assigned', 'Job Assigned'), ('started', 'Job Started'), ('closed', 'Job closed'), ('deffered', 'Job Deffered'), ('reopen', 'Job Reopen')], default='unassigned', max_length=20, verbose_name='Status')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')),
                ('created_at', models.DateTimeField(blank=True, help_text="This is the Creation time used for ticket creation, assignment, reporting and insight INTO THE FUTURE based on '8am-5pm' or '24/7' vendor configuration", null=True, verbose_name='Scheduled Time')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time Modified')),
                ('arrival_time', models.DateTimeField(blank=True, null=True, verbose_name='First Time Vendor Arrival')),
                ('remarks', models.TextField(blank=True, max_length=3500, null=True, verbose_name='Recommendation')),
                ('remarks_date', models.DateTimeField(blank=True, null=True, verbose_name='Recommend Time')),
                ('paused_by_system', models.BooleanField(default=False, verbose_name='System Paused')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticketbranch', to='general_settings.branch', verbose_name='Branch')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticketcategory', to='general_settings.category', verbose_name='Category')),
                ('checklist', models.ManyToManyField(related_name='checklists', to='general_settings.checklist', verbose_name='Checklist')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticketcreator', to=settings.AUTH_USER_MODEL, verbose_name='Staff')),
                ('sla_exception', models.ManyToManyField(related_name='slaexceptions', to='general_settings.slaexceptions', verbose_name='SLA Exception')),
                ('team', models.ForeignKey(help_text='Team responsible for this task', on_delete=django.db.models.deletion.PROTECT, related_name='ticketteam', to='vendors.team', verbose_name='Team')),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticketterminal', to='general_settings.terminals', verbose_name='Terminal')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='AssignMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Assign On')),
                ('arrival_time', models.DateTimeField(blank=True, null=True, verbose_name='Journey Starts')),
                ('arrival_confirm', models.DateTimeField(blank=True, null=True, verbose_name='Confirmed Arrival')),
                ('completion_time', models.DateTimeField(blank=True, null=True, verbose_name='Closure Time')),
                ('total_minutes', models.PositiveIntegerField(default=0, verbose_name='Total Minutes worked')),
                ('deffered_count', models.PositiveIntegerField(default=0, verbose_name='Deffered Count')),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignees', to=settings.AUTH_USER_MODEL, verbose_name='Team Member')),
                ('assignor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignors', to=settings.AUTH_USER_MODEL, verbose_name='Assignor')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignteam', to='vendors.team', verbose_name='Team')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignticket', to='tickets.ticket', verbose_name='Ticket')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticketterminal', to='general_settings.vendorcompany', verbose_name='Vendor')),
            ],
            options={
                'verbose_name': 'Assign Ticket',
                'verbose_name_plural': 'Assign Tickets',
                'ordering': ('-pk',),
            },
        ),
    ]
