import pyqrcode
import png
from django.conf import settings


def get_qr_code(url):
    qr = pyqrcode.QRCode(url)
    qr.png('static/images/qr.png', scale=5)
    print('\a\a\a')
