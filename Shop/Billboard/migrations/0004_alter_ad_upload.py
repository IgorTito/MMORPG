# Generated by Django 4.0.6 on 2022-07-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard', '0003_alter_ad_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='media/uploads/', verbose_name='Загрузить файл'),
        ),
    ]