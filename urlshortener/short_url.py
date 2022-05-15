import shortuuid
from django.conf import settings


def get_short_url(n=5):
    return str(shortuuid.ShortUUID().random(length=n))
