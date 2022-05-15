from django.db import models
# import string
from .short_url import get_short_url
from pyqrcode import QRCode
from datetime import datetime, date
from django.urls import reverse
import png
from django.conf import settings


# Create your models here.
class Link(models.Model):
    """
    Represents a Link
    """
    # id = models.BigAutoField()
    short_url = models.CharField(max_length=255, help_text='Short url', default=get_short_url, primary_key=True,
                                 verbose_name='Короткая ссылка')
    full_url = models.URLField(max_length=2000, help_text='Source url', verbose_name='Ссылка')
    # qr_code = models.ImageField(upload_to='qrcodes/')
    expiration_date = models.DateField(null=True, blank=True, verbose_name='Дата уничтожения')
    creation_date = models.DateField(default=datetime.now, verbose_name='Дата создания')
    count_clicked = models.IntegerField(default=0, verbose_name='Кол-во переходов')

    def get_absolute_url(self):
        return reverse('shorten', kwargs={'surl': self.short_url})

    def __str__(self):
        return self.short_url

    def clicked(self):
        self.count_clicked += 1

    def is_expired(self):
        if self.expiration_date is None:
            return False

        today = date.today()
        # return datetime.now() >= self.expiration_date
        return datetime(today.year, today.month, today.day) >= self.expiration_date

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ['creation_date', 'expiration_date']


class Stats(models.Model):
    target = models.ForeignKey(Link, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, editable=False)
    referer = models.URLField(blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(blank=True, max_length=100, null=True)
