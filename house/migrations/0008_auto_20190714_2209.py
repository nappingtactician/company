# Generated by Django 2.2.3 on 2019-07-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_auto_20190714_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='asset',
            name='assetid',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='work',
            name='task_act',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='work',
            name='task_freq',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='work',
            name='taskid',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='worker',
            name='workerid',
            field=models.CharField(default='', max_length=25),
        ),
    ]
