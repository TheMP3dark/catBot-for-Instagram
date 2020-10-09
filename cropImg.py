# crop image into a square using PIL
from PIL import Image

def cropCatImg():
    im = Image.open("tempCatImg.jpg")
    width, height = im.size

    print(width, height)

    if width==height:
        im.save("final.jpg")
    elif width > height:
        d = width - height
        left = d/2
        top = 0
        right = width-(d/2)
        bottom = height
        im1 = im.crop((left - 1, top - 1, right - 1, bottom + 1))
        im1.show()
        im1.save("final.jpg")


