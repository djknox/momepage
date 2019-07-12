# Generated by Django 2.2.3 on 2019-07-11 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the cohort here.', max_length=300)),
                ('start_date', models.DateField(blank=True, help_text='Enter the start date for the cohort here.', null=True)),
                ('end_date', models.DateField(blank=True, help_text='Enter the end date for the cohort here.', null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the day here.', max_length=300)),
                ('date', models.DateField(help_text='Enter the date of the day here.', unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cohort')),
            ],
        ),
    ]