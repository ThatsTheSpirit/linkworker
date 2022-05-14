import pyqrcode
import png
from django.conf import settings

def get_qr_code(url):
    url_base = '127.0.0.1'
    qr = pyqrcode.QRCode(url_base + '/' + url)
    qr.png(f'{settings.STATIC_URL}images/qr.png')
    print('\a\a\a')
