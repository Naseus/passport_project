# Generated by Django 3.0.6 on 2020-08-13 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('ext_address', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=5, null=True)),
                ('country', models.CharField(default='US', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('role', models.CharField(choices=[('student', 'Student'), ('prospective', 'Prospective '), ('avtechemployee', 'AVTech Employee'), ('instructor', 'Instructor'), ('instructor_contractor', 'Instructor - Adjunct'), ('vendor_institutional', 'Vendor - Institutional'), ('vendor_government', 'Vendor - Government'), ('vendor_business', 'Vendor - Business')], max_length=32)),
                ('avtech_department', models.CharField(choices=[('administration', 'Administration'), ('admission', 'Admission'), ('marketing', 'Marketing'), ('sales', 'Sales'), ('humanresources', 'Human Resources'), ('careerservices', 'Career Services'), ('finance', 'Finannce'), ('staff', 'Staff'), ('faculty', 'Faculty')], max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_list_userprofiles', 'List All User Profiles'),),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('company_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=32)),
                ('desc', models.TextField(blank=True)),
                ('home_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('cell_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('title', models.CharField(max_length=32)),
                ('salutation', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('None', 'None')], default='None', max_length=8)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Address')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
