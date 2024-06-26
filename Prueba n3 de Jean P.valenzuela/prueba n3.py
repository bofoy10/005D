import json

with open("biblioteca.json" "r")as archivo:
    leer_json = json.load(archivo)

    AutorID = input('Ingrese su autor: ')
    nombre = input('Ingrese su autor: ')
    nacionalidadid = input('Ingrese la nacionalidad del autor: ')

autor = [{
    'id' : AutorID,
    'nombre_id': nombre,
    'nacionalidad': nacionalidadid,
}]

