from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ad_theme = models.CharField(max_length=64, verbose_name="Заголовок")
    date_of_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    text_of_ad = models.TextField(verbose_name="Текст объявлениея")
    rating = models.SmallIntegerField(default=0, verbose_name="Рейтинг")

    TANKS = "tn"
    HEALS = "hl"
    DD = "dd"
    TRADERS = "tr"
    GILDMASTERS = "gm"
    QUESTGIVERS = "qg"
    BLACKSMITH = "bs"
    TANNER = "ta"
    POTION = "pt"
    MASTERS = "ms"

    CATEGORY = (
        ("tn", "Танки"),
        ("hl", "Хилы"),
        ("dd", "ДД"),
        ("tr", "Торговцы"),
        ("gm", "Гилдмастеры"),
        ("qg", "Квестгиверы"),
        ("bs", "Кузнецы"),
        ("ta", "Кожевники"),
        ("pt", "Зельевары"),
        ("ms", "Мастера заклинаний"),
    )
    categoryAd = models.CharField(max_length=2, choices=CATEGORY, verbose_name="Категория")
    upload_file = models.FileField(upload_to="uploads/", null=True, blank=True, verbose_name="Файл")
    upload_image = models.ImageField(upload_to="uploads/", null=True, blank=True, verbose_name="Изображение")

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/'

    class Meta():
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Echo(models.Model):
    echo_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Автор комментария")
    echo_text = models.TextField(max_length=512, verbose_name="Текст комментария")
    echo_ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление", related_name="echo_ads")
    echo_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    echo_status = models.BooleanField(default=False)

    class Meta():
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"

    def __str__(self):
        return f"{self.echo_text}"

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/'