
from django.dispatch import receiver

from .models import *
from django.core.mail import send_mail
from django.db.models.signals import post_save


@receiver(post_save, sender=Echo)
def notify_echo(instance, **kwargs):

    subject = instance.echo_ad.ad_theme
    print(subject)
    print('**************')
    user_echo = instance.echo_author
    author_ad = instance.echo_ad.author
    send_mail(
        subject=subject,
        message=f"Здравствуйте, {author_ad}\n"
                f"cообщаем, что на Ваше объявление появился отклик\n"
                f"от пользователя - {user_echo} \n"
                f"краткий текст сообщения - {instance.echo_text[:20]} \n"
                f"полный текст сообщения в Вашем личном кабинете",
        from_email='hayabusaigor@yandex.ru',
        recipient_list=[author_ad.email]
    )
