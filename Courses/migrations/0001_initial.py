# Generated by Django 5.2 on 2025-04-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('NumofStudents', models.IntegerField()),
                ('Category', models.CharField(max_length=100)),
                ('Duration', models.IntegerField()),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
            ],
        ),
    ]
