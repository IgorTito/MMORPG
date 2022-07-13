# Generated by Django 4.0.6 on 2022-07-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard', '0004_alter_ad_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='upload',
        ),
        migrations.AddField(
            model_name='ad',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Файл'),
        ),
        migrations.AddField(
            model_name='ad',
            name='upload_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Изображение'),
        ),
    ]