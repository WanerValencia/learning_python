# name
# last_name
# email
# age
# number


jose = {
    'name': 'jose luis',
    'last_name': 'rivera',
    'email': 'jose@asd.com',
    'age': 22,
    'number': 3133333,
}

mario = {
    'last_name': 'gutierrez',
    'email': 'mario@asd.com',
    'age': 44,
    'number': 433333,
}

luz = {
    'name': 'luz',
    'last_name': 'ospina',
    'email': 'luz@asd.com',
    'age': 37,
    'number': 9199933,
}

promedio_edad = (luz.get('age') + mario.get('age') + jose.get('age')) / 3

print(float(promedio_edad))

print(luz.get('name', 'no pude obtenerlo'))
print(mario.get('name', 'no pude obtenerlo'))
print(jose.get('name', 'no lo pude obtener'))


luz['city'] = 'pereira'
mario['city'] = 'bogota'
jose['city'] = 'cali'

print(luz.get('city', 'no pude obtenerlo'))
print(mario.get('city', 'no pude obtenerlo'))
print(jose.get('city', 'no lo pude obtener'))