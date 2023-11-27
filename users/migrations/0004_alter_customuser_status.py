# Generated by Django 4.2 on 2023-11-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('learner', 'learner'), ('tutor', 'tutor')], default='learner', max_length=100),
        ),
    ]