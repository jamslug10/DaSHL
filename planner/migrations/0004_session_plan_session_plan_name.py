# Generated by Django 3.1.4 on 2020-12-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_auto_20201212_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='session_plan',
            name='session_plan_name',
            field=models.CharField(default='ingrese un nombre', max_length=200),
        ),
    ]
