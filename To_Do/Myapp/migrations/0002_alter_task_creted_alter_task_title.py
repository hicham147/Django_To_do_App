# Generated by Django 4.0.3 on 2022-05-30 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creted',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]