# Generated by Django 3.2.9 on 2022-04-27 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_aim_taskaim'),
    ]

    operations = [
        migrations.AddField(
            model_name='aim',
            name='taskCur',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
    ]
