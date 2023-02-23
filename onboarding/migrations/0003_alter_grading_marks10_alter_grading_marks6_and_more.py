# Generated by Django 4.1.3 on 2023-02-21 21:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0002_alter_grading_marks10_alter_grading_marks6_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grading',
            name='marks10',
            field=models.PositiveIntegerField(choices=[(0, '0 Mark'), (1, '1 Mark'), (2, '2 Marks'), (3, '3 Marks'), (4, '4 Marks'), (5, '5 Marks')], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Marks 10'),
        ),
        migrations.AlterField(
            model_name='grading',
            name='marks6',
            field=models.PositiveIntegerField(choices=[(0, '0 Mark'), (1, '1 Mark'), (2, '2 Marks'), (3, '3 Marks'), (4, '4 Marks'), (5, '5 Marks')], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Marks 6'),
        ),
        migrations.AlterField(
            model_name='grading',
            name='marks7',
            field=models.PositiveIntegerField(choices=[(0, '0 Mark'), (1, '1 Mark'), (2, '2 Marks'), (3, '3 Marks'), (4, '4 Marks'), (5, '5 Marks')], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Marks 7'),
        ),
        migrations.AlterField(
            model_name='grading',
            name='marks8',
            field=models.PositiveIntegerField(choices=[(0, '0 Mark'), (1, '1 Mark'), (2, '2 Marks'), (3, '3 Marks'), (4, '4 Marks'), (5, '5 Marks')], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Marks 8'),
        ),
        migrations.AlterField(
            model_name='grading',
            name='marks9',
            field=models.PositiveIntegerField(choices=[(0, '0 Mark'), (1, '1 Mark'), (2, '2 Marks'), (3, '3 Marks'), (4, '4 Marks'), (5, '5 Marks')], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Marks 9'),
        ),
    ]
