from PIL import Image
from img import *
# from card import *

im = Image.open('game.jpg')
pix = im.load()

print(Color.color_all(pix, im.size))

im.save('2.jpg')