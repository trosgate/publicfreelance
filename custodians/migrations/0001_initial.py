# Generated by Django 4.1.3 on 2023-02-20 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_settings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpDesk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title field is Required', max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('content', models.TextField(max_length=2000, verbose_name='Message')),
                ('reference', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Reference #')),
                ('status', models.CharField(choices=[('active', 'Active'), ('closed', 'Closed')], default='active', max_length=20, verbose_name='Status')),
                ('condition', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=100, verbose_name='Priority Level')),
                ('file', models.ImageField(blank=True, null=True, upload_to='complaint_file_path/', verbose_name='Attachment(Optional)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time Created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time Modified')),
                ('is_routed', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestcategory', to='general_settings.category', verbose_name='Category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdstaff', to=settings.AUTH_USER_MODEL, verbose_name='Request Staff')),
                ('request_branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requester', to='general_settings.branch', verbose_name='Request Branch')),
                ('support_branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supporter', to='general_settings.branch', verbose_name='Support Team')),
                ('support_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supportstaff', to=settings.AUTH_USER_MODEL, verbose_name='Support Staff')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='HelpDeskMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=2000, verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time Created')),
                ('action', models.BooleanField(choices=[(False, 'Customer Replied'), (True, 'Admin Replied')], default=True, verbose_name='Action')),
                ('helpdesk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deskreplies', to='custodians.helpdesk', verbose_name='HelpDesk')),
                ('support', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ticketsupport', to=settings.AUTH_USER_MODEL, verbose_name='Support')),
            ],
            options={
                'verbose_name': 'HelpDesk Reply',
                'verbose_name_plural': 'HelpDesk Replies',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Custodian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10, verbose_name='Gender')),
                ('tagline', models.CharField(blank=True, max_length=100, verbose_name='Tagline')),
                ('description', models.TextField(blank=True, error_messages={'name': {'max_length': 'Ensure a maximum character of 2000 for description field'}}, max_length=2000, verbose_name='Description')),
                ('profile_photo', models.ImageField(default='profile/user-login.png', upload_to='profile_image_path/', verbose_name='Profile Photo')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Residence Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='custodian', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Staff Profile',
                'verbose_name_plural': 'Staffs Profile',
            },
        ),
    ]
