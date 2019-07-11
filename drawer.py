from PIL import Image, ImageDraw, ImageFont
from constants import *


def create_image(users):
    """
    Crea una imagen a partir de la información de los usuarios.
    :param users: lista de usuarios (objeto JSON parseado)
    :return:
    """
    image = Image.new('RGB', IMAGE_SIZE, color=BACKGROUND_COLOR)
    font = ImageFont.truetype(FONT_FILE, FONT_SIZE)

    draw = ImageDraw.Draw(image)

    # Posición de los nombres sobre la imagen
    pointer = [10, 10]

    for i in users:
        text_size = draw.textsize(i['nombre'], font=font)

        if (pointer[1] + 10 + text_size[1]) >= IMAGE_SIZE[1]:
            print("ERROR: no caben los nombres con la configuración actual, reduce el "
                  "número de nombre o el tamaño de la fuente.")
            return -1

        if (pointer[0] + 20 + text_size[0]) >= IMAGE_SIZE[0]:
            pointer[0] = 10
            pointer[1] += 10 + text_size[1]

        if i['estado'] == "muerto":
            color = (255, 0, 0)
            # draw.line((x0, y0, x1, y1))
            draw.line((pointer[0],
                       pointer[1] + (text_size[1] / 2),
                       pointer[0] + text_size[0],
                       pointer[1] + (text_size[1] / 2)),
                      fill=(255, 0, 0), width=2)
        else:
            color = (0, 0, 0)

        draw.text(pointer, i['nombre'], font=font, fill=color)
        pointer[0] += 20 + text_size[0]

    image.save(IMAGE_FILE)
    return 0
