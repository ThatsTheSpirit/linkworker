import pyqrcode
import png

def get_qr_code(url):
    url_base = '127.0.0.1'
    qr = pyqrcode.QRCode(url_base + '/' + url)
    qr.png('qr.png')
    print('\a\a\a')
