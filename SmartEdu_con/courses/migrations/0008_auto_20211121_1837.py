# Generated by Django 3.2.9 on 2021-11-21 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20211121_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
