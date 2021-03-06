# Generated by Django 4.0.1 on 2022-02-07 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_status', models.CharField(choices=[('PENDING', 'PENDING'), ('IN_PROGRESS', 'INPROGRESS'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=100)),
                ('current_status', models.CharField(choices=[('PENDING', 'PENDING'), ('IN_PROGRESS', 'INPROGRESS'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=100)),
                ('change_date', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
