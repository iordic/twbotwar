from PIL import Image, ImageDraw, ImageFont
import json

FONT_FILE = '../assets/Grundschrift-Regular.otf'
USERS_FILE = '../data/usuarios.json'
IMAGE_FILE = 'example.png'

IMAGE_SIZE = (800, 600)
FONT_SIZE = 20

BACKGROUND_COLOR = (255, 237, 115)  # RGB decimal


def generar_imagen(lista):
    image = Image.new('RGB', IMAGE_SIZE, color=BACKGROUND_COLOR)
    font =  ImageFont.truetype(FONT_FILE, FONT_SIZE)
    
    draw = ImageDraw.Draw(image)
    
    # Posición de inicio donde colocaremos los nombres
    pointer = [10, 10]

    for i in lista:
        text_size = draw.textsize(i['nombre'], font=font)

        if (pointer[1] + 10 + text_size[1]) >= IMAGE_SIZE[1]:
            print("No caben todos los nombres, algunos se han omitido")
            image.save(IMAGE_FILE)
            return

        if (pointer[0] + 20 + text_size[0]) >= IMAGE_SIZE[0]:
            pointer[0] = 10
            pointer[1] += 10 + text_size[1]

        if i['estado'] == "muerto":
            color = (255,0,0)
            # draw.line((x0, y0, x1, y1))
            draw.line((pointer[0],
                       pointer[1] + (text_size[1]/2),
                       pointer[0] + text_size[0],
                       pointer[1] + (text_size[1]/2)),
                      fill=(255,0,0), width=2)
        else:
            color = (0,0,0)

        draw.text(pointer, i['nombre'], font=font, fill=color)
        
        pointer[0] += 20 + text_size[0]

    image.save(IMAGE_FILE)


if __name__ == '__main__':
    with open(USERS_FILE) as json_file:
        data = json_file.read()

    usuarios = json.loads(data)
    # Si queremos comprobar que lo carga bien:
    # print(json.dumps(usuarios, indent=4))
    generar_imagen(usuarios)
