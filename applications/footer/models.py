from django.core.validators import FileExtensionValidator
from django.db import models


class FirstFooterTab(models.Model):
    icon = models.FileField(validators=[
        FileExtensionValidator(
            allowed_extensions=[
                'svg',
                'png',
                'eps',
                'pdf',
            ], message='Неправильный формат!'
        )
    ])
    info = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20, default='(555) 555 555')

    def save(self, *args, **kwargs):
        self.phone_num = '+996 ' + self.phone_num
        super(FirstFooterTab, self).save(*args, **kwargs)


class SecondFooterTab(models.Model):
    MESSENGER_TYPE = (
        ('W/A', 'WhatsApp'),
        ('TG', 'Telegram'),
        ('ML', 'Mail'),
        ('INS', 'Instagram'),
        ('PN', 'Phone'),
    )
    messenger = models.CharField(max_length=30, choices=MESSENGER_TYPE)
    url_or_phone = models.URLField(max_length=255)

    def save(self, *args, **kwargs):
        if self.messenger == 'W/A':
            self.url_or_phone = f'https://wa.me{self.url_or_phone}'
        else:
            self.url_or_phone = self.url_or_phone
        super(SecondFooterTab, self).save(*args, **kwargs)