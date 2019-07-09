from PIL import Image, ImageDraw, ImageFont
import pprint
import json

# Ejemplo simple de uso de pillow para los nombres
usuarios = '[{"nombre":"Maria", "estado":"muerto"},\
             {"nombre":"Pepe", "estado":"muerto"},\
             {"nombre":"Rosa", "estado":"muerto"},\
             {"nombre":"Juan", "estado":"muerto"},\
             {"nombre":"Christian", "estado":"vivo"},\
             {"nombre":"Ximo", "estado":"muerto"},\
             {"nombre":"Inés", "estado":"vivo"},\
             {"nombre":"Cristina", "estado":"muerto"},\
             {"nombre":"Juanjo", "estado":"vivo"},\
             {"nombre":"Alfonso", "estado":"vivo"},\
             {"nombre":"Álvaro", "estado":"muerto"},\
             {"nombre":"Estefania", "estado":"vivo"},\
             {"nombre":"Sara", "estado":"vivo"},\
             {"nombre":"Alberto", "estado":"vivo"},\
             {"nombre":"Narciso", "estado":"vivo"},\
             {"nombre":"Roxanne", "estado":"muerto"},\
             {"nombre":"Berta", "estado":"vivo"},\
             {"nombre":"Alicia", "estado":"vivo"},\
             {"nombre":"Bob", "estado":"muerto"},\
             {"nombre":"Eve", "estado":"vivo"},\
             {"nombre":"Alba", "estado":"vivo"},\
             {"nombre":"Jose", "estado":"muerto"}]'

image_size = (800, 600)


def generar_imagen(lista):
    image = Image.new('RGB', image_size, color=(166, 211, 243))
    font =  ImageFont.truetype('Grundschrift-Regular.otf', 16)
    
    draw = ImageDraw.Draw(image)
    
    # Posición de inicio donde colocaremos los nombres
    pointer = [10, 10]

    for i in lista:
        text_size = draw.textsize(i['nombre'], font=font)
        if i['estado'] == "muerto":
            color = (255,0,0)
            # draw.line((x0, y0, x1, y1))
            draw.line((pointer[0], pointer[1] + (text_size[1]/2), pointer[0] + text_size[0], pointer[1] + (text_size[1]/2)), 
                    fill=(255,0,0), width=2)
        else:
            color = (0,0,0)

        if (pointer[0] + 20 + text_size[0]) >= image_size[0]:
            pointer[0] = 10
            pointer[1] += 10 + text_size[1]
        draw.text(pointer, i['nombre'], font=font, fill=color)
        
        pointer[0] += 20 + text_size[0]

    image.save('example.png')



if __name__ == '__main__':
    datos = json.loads(usuarios)
    # Si queremos comprobar que lo carga bien:
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(datos)
    generar_imagen(datos)
