
from django.dispatch import receiver

from .models import *
from django.core.mail import send_mail
from django.db.models.signals import post_save


@receiver(post_save, sender=Echo)
def notify_echo(instance, created, **kwargs):
    if created:
        subject = f'{instance.echo_author}'

    send_mail(
        subject=subject,
        message=f"Здравствуйте, {User.objects.get(ad=instance.author)}\n"                
                f"cообщаем, что на Ваше объявление появился отклик\n"
                f"от пользователя - {instance.echo_author} \n"
                f"краткий текст сообщения - {instance.echo_text[:20]} \n"
                f"полный текст сообщения в Вашем личном кабинете",
        from_email='hayabusaigor@yandex.ru',
        # recipient_list=[.email]
    )


post_save.connect(notify_echo, sender=Echo)