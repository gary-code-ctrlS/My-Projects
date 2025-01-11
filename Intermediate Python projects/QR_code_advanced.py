import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=10,)                  #Dimensions
qr.add_data("https://www.youtube.com/watch?v=fn9fqTUHl7Q&list=PLfP6i5T0-DkJKnpagTFIM7KxQy9FILIOO")  #URL
qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color="black")  #FG and BG color
img.save("temp_music.png")