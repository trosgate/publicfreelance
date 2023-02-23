# Generated by Django 4.1.3 on 2023-02-20 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The Short title that fits your service', max_length=100, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=20, verbose_name='Team Status')),
                ('purpose', models.TextField(blank=True, null=True, verbose_name='Purpose')),
                ('ordering', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Order Priority')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teammanager', to=settings.AUTH_USER_MODEL, verbose_name='Team Founder')),
                ('members', models.ManyToManyField(related_name='team_member', to=settings.AUTH_USER_MODEL, verbose_name='Team Members')),
            ],
            options={
                'verbose_name': 'Vendor Team',
                'verbose_name_plural': 'Vendors Teams',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10, verbose_name='Gender')),
                ('tagline', models.CharField(blank=True, max_length=100, verbose_name='Tagline')),
                ('description', models.TextField(blank=True, error_messages={'name': {'max_length': 'Ensure a maximum character of 2000 for description field'}}, max_length=2000, verbose_name='Description')),
                ('profile_photo', models.ImageField(default='profile/user-login.png', upload_to='profile_image_path/', verbose_name='Profile Photo')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Residence Address')),
                ('active_team_id', models.PositiveIntegerField(default=0, verbose_name='Active Team ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Vendor Profile',
                'verbose_name_plural': 'Vendor Profile',
            },
        ),
        migrations.CreateModel(
            name='TeamChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('is_sent', models.BooleanField(default=False)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamsender', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamchats', to='vendors.team', verbose_name='Chat Team')),
            ],
            options={
                'ordering': ['sent_on'],
            },
        ),
    ]
