import os
import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=IUAUyR07wHo&ab_channel=wherebear")

img.save("qr.png", "PNG")
os.system("open qr.png")