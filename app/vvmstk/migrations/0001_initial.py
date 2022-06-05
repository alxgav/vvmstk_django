# Generated by Django 4.0.1 on 2022-06-03 13:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups_students',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=4, verbose_name='group number')),
                ('group_date_begin', models.DateField(verbose_name='start date')),
                ('group_date_end', models.DateField(verbose_name='end date')),
                ('kategory', models.CharField(choices=[('B1', 'B1'), ('B', 'B'), ('C1', 'C1'), ('C', 'C')], max_length=52, verbose_name='drive kategory')),
                ('price', models.IntegerField(verbose_name='price')),
                ('time_study', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='learning time')),
            ],
            options={
                'verbose_name': 'groups of students',
                'verbose_name_plural': 'groups of students',
                'db_table': 'content"."groups_students',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=255, verbose_name='surname')),
                ('firstname', models.CharField(max_length=255, verbose_name='firstname')),
                ('middlename', models.CharField(max_length=255, verbose_name='middlename')),
                ('birth_date', models.DateField(verbose_name='birthday')),
                ('inn_code', models.CharField(max_length=10, verbose_name='inn')),
                ('birthplace', models.CharField(max_length=255, verbose_name='birthplace')),
                ('address', models.TextField(verbose_name='address')),
                ('pass_num', models.CharField(max_length=10, verbose_name='passport number')),
                ('pass_date', models.DateField(verbose_name='passport date')),
                ('pass_plase', models.TextField(verbose_name='passport place')),
                ('hospital_num', models.CharField(max_length=10, verbose_name='hospital number')),
                ('hospital_date', models.DateField(verbose_name='hospital date')),
                ('hospital_plase', models.TextField(verbose_name='hospital place')),
                ('id_groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vvmstk.groups_students')),
            ],
            options={
                'verbose_name': 'students',
                'verbose_name_plural': 'students',
                'db_table': 'content"."students',
            },
        ),
    ]