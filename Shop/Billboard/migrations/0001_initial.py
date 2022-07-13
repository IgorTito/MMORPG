# Generated by Django 4.0.6 on 2022-07-05 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_theme', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('date_of_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('text_of_ad', models.TextField(verbose_name='Текст объявлениея')),
                ('rating', models.SmallIntegerField(default=0, verbose_name='Рейтинг')),
                ('categoryAd', models.CharField(choices=[('tn', 'Танки'), ('hl', 'Хилы'), ('dd', 'ДД'), ('tr', 'Торговцы'), ('gm', 'Гилдмастеры'), ('qg', 'Квестгиверы'), ('bs', 'Кузнецы'), ('ta', 'Кожевники'), ('pt', 'Зельевары'), ('ms', 'Мастера заклинаний')], max_length=2, verbose_name='Категория')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Echo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('echo_text', models.TextField(max_length=512)),
                ('echo_date', models.DateTimeField(auto_now_add=True)),
                ('echo_ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Billboard.ad')),
                ('echo_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
            },
        ),
    ]
