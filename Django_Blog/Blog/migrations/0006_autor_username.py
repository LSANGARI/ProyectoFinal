# Generated by Django 4.1.3 on 2022-11-14 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_alter_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre Usuario'),
        ),
    ]