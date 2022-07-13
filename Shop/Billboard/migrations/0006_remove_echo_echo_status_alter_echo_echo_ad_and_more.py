# Generated by Django 4.0.6 on 2022-07-11 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Billboard', '0005_remove_ad_upload_ad_upload_file_ad_upload_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='echo',
            name='echo_status',
        ),
        migrations.AlterField(
            model_name='echo',
            name='echo_ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='echo_ads', to='Billboard.ad', verbose_name='Объявление'),
        ),
        migrations.AlterField(
            model_name='echo',
            name='echo_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
        migrations.AlterField(
            model_name='echo',
            name='echo_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='echo',
            name='echo_text',
            field=models.TextField(max_length=512, verbose_name='Текст комментария'),
        ),
    ]