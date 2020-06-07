# Generated by Django 3.0.6 on 2020-06-04 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='type',
            field=models.CharField(choices=[('student', 'Student'), ('avtechemployee', 'AVTech Employee'), ('instructor', 'Instructor')], default='', max_length=32),
            preserve_default=False,
        ),
    ]