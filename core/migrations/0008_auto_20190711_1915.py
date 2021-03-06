# Generated by Django 2.2.3 on 2019-07-12 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_guestlecture_speaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestlecture',
            name='end_time',
            field=models.TimeField(help_text='Enter the time when the guest lecture will end.'),
        ),
        migrations.AlterField(
            model_name='guestlecture',
            name='start_time',
            field=models.TimeField(help_text='Enter the time when the guest lecture will start.'),
        ),
        migrations.CreateModel(
            name='FieldTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(help_text='Enter the time when the field trip will start.')),
                ('end_time', models.TimeField(help_text='Enter the time when the field trip will end.')),
                ('company', models.CharField(help_text='Enter the name of the company here.', max_length=300)),
                ('description', models.TextField(help_text='Enter the description of the field trip here.')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Day')),
            ],
        ),
    ]
