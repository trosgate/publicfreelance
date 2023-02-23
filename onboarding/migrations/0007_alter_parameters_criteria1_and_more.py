# Generated by Django 4.1.3 on 2023-02-22 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0006_remove_parameters_created_by_remove_parameters_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameters',
            name='criteria1',
            field=models.CharField(default='Criteria 1', max_length=100, unique=True, verbose_name='Criteria 1'),
        ),
        migrations.AlterField(
            model_name='parameters',
            name='criteria2',
            field=models.CharField(default='Criteria 2', max_length=100, unique=True, verbose_name='Criteria 2'),
        ),
        migrations.AlterField(
            model_name='parameters',
            name='criteria3',
            field=models.CharField(default='Criteria 3', max_length=100, unique=True, verbose_name='Criteria 3'),
        ),
        migrations.AlterField(
            model_name='parameters',
            name='criteria4',
            field=models.CharField(default='Criteria 4', max_length=100, unique=True, verbose_name='Criteria 4'),
        ),
        migrations.AlterField(
            model_name='parameters',
            name='criteria5',
            field=models.CharField(default='Criteria 5', max_length=100, unique=True, verbose_name='Criteria 5'),
        ),
        migrations.AlterField(
            model_name='parameters',
            name='criteria6',
            field=models.CharField(default='Criteria 6', max_length=100, unique=True, verbose_name='Criteria 6'),
        ),
    ]
