# Generated by Django 4.1.3 on 2023-02-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.CharField(blank=True, default='Control access with token and vendor permission', max_length=100)),
                ('token_authenticator', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=False, help_text='By default, all users(excluding Staff) will be able to login to dashoard using EMAIL and PASSWORD. This plugin will (1) Present extra Token form after login, (2) Send simple mail alert containingg token, (3) button to resend token if customer has not received, (4) Then a valid token entered will log user to dashboard', verbose_name='2FA Mailer')),
                ('vendor_role', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Activated')], default=True, help_text='By default, only administrator can create vendor with full permission. This feature gives moderating vendor the right to upgrade or downgrade other team members', verbose_name='Vendor Team Upgrade')),
            ],
            options={
                'verbose_name': 'Authenticator Plugin',
                'verbose_name_plural': 'Authenticator Plugins',
            },
        ),
        migrations.CreateModel(
            name='Notifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.CharField(default='Allow or disable email alerts by notification centers', max_length=100)),
                ('mailing_group', models.BooleanField(choices=[(False, 'Alert Cluster by Branch'), (True, 'Alert all Cluster Group')], default=True, help_text="This plugin determines whether cluster should be copied in mail for only their 'managed branches' or in 'all branches' alerts", verbose_name='Mailing Group Alert')),
                ('open_ticket', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=True, help_text='This will enable or disable the notifications when ticket is CREATED', verbose_name='Open Ticket Alert')),
                ('assign_ticket', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=True, help_text='This will enable or disable the notifications when ticket is ASSIGNED', verbose_name='Assign Ticket Alert')),
                ('started_ticket', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=False, help_text='This will enable or disable the notifications when ticket is STARTED/ONGOING', verbose_name='Ongoing Ticket Alert')),
                ('deferred_ticket', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=False, help_text='This will enable or disable the notifications when ticket is PAUSED, excluding actions performed by system', verbose_name='Paused Ticket Alert')),
                ('reopen_ticket', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=False, help_text='This will enable or disable the notifications when ticket is REOPEN, excluding actions performed by system', verbose_name='Reopen Ticket Alert')),
                ('closed_ticket', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=True, help_text='This will enable or disable the notifications when ticket is CLOSED', verbose_name='Closed Ticket Alert')),
                ('remarks', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=True, help_text='This will enable or disable the notifications when ticket REMARK is submitted by vendor', verbose_name='Ticket Remark Alert')),
                ('complaint_created', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=True, help_text='This will enable or disable the notifications when COMPLAINT is submitted', verbose_name='New Branch Complaint Alert')),
                ('complaint_routing', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=True, help_text='This will enable or disable the notifications when COMPLAINT is re-routed', verbose_name='Complaint Re-Routing Alert')),
                ('complaint_reply', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=True, help_text='This will enable or disable the notifications when COMPLAINT is replied', verbose_name='Complaint Reply Alert')),
                ('requisition_created', models.BooleanField(choices=[(False, 'Disabled'), (True, 'Launched')], default=True, help_text='This will enable or disable the notifications when REQUISITION is CREATED', verbose_name='New Requisition Alert')),
            ],
            options={
                'verbose_name': 'Notifier Plugin',
                'verbose_name_plural': 'Notifier Plugins',
            },
        ),
    ]
