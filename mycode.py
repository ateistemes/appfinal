from PIL import Image, ImageDraw
def grey(image):
    draw = ImageDraw.Draw(image)
    pix = image.load()
    for i in range(image.width):
        for j in range(image.height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            draw.point((i, j), (S, S, S))
    image.save("res.jpg", "JPEG")
    del draw
def sepia(image):
    depth = 50
    draw = ImageDraw.Draw(image)
    pix = image.load()
    for i in range(image.width):
        for j in range(image.height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            a = S + depth * 2
            b = S + depth
            c = S
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
    image.save("sepia.jpg", "JPEG")
    del draw
def blacwhite(image):
    draw = ImageDraw.Draw(image)
    pix = image.load()
    for i in range(image.width):
        for j in range(image.height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if (S > (((255 + 5) // 2) * 3)):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    image.save('blackandwhite.jpg', 'JPEG')
    del draw
def negative(image):
    draw = ImageDraw.Draw(image)
    pix = image.load()
    for i in range(image.width):
        for j in range(image.height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))
    image.save("negative.jpg", "JPEG")
    del draw

