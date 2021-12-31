import pyqrcode 
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Ahmet İle Kod Yazıyoruz")
qr.png("QR_kodum.png", scale=8)