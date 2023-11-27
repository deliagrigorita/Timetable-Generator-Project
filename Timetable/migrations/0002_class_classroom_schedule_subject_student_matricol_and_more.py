# Generated by Django 4.2.7 on 2023-11-27 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=15)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='matricol',
            field=models.CharField(default='111222333444', max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=20, null=True)),
                ('academic_year', models.CharField(max_length=10, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Timetable.class')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(default='Please add description', max_length=128)),
                ('availability', models.BooleanField(default=True)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Timetable.classroom')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Timetable.classroom'),
        ),
        migrations.AddField(
            model_name='class',
            name='resources',
            field=models.ManyToManyField(to='Timetable.resource'),
        ),
        migrations.AddField(
            model_name='class',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Timetable.schedule'),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='Timetable.student'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Timetable.teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='name',
            field=models.ManyToManyField(to='Timetable.subject'),
        ),
    ]
