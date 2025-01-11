import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=fn9fqTUHl7Q&list=PLfP6i5T0-DkJKnpagTFIM7KxQy9FILIOO")
img.save("music_temp.png")
