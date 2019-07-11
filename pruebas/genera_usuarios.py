import random
import pprint
import json


NAMES_FILE = 'nombres.csv'
EXPORT_FILE = '../data/usuarios.json'
CANTIDAD = 200

def main():
    nombres = []
    estados = ['vivo', 'muerto']
    usuarios = []

    # Cargamos el diccionario de nombres
    with open(NAMES_FILE) as file:
        for line in file:
            nombres.append(line.strip())
        file.close()

    # Elegimos 100 al azar
    for i in range(0, CANTIDAD):
        usuario = {}
        # Asignamos valores aleatorios
        usuario['nombre'] = random.choice(nombres)
        usuario['estado'] = random.choice(estados)
        usuario['seguidores'] = random.randint(0, 1000000)
        # Añadimos a la colección
        usuarios.append(usuario)

    with open(EXPORT_FILE, 'w') as outfile:
        json.dump(usuarios, outfile, indent=4)


if __name__ == '__main__':
    main()
