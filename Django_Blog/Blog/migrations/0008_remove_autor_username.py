# Generated by Django 4.1.3 on 2022-11-14 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_alter_autor_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='username',
        ),
    ]
