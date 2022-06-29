# comentarios de una linea
# username = user.pop('username')
# print(username)
# print(user)

"""
comentarios de varias lineas
print("Hola")
"""


#OBJECTS - DICTS
user = {
    'username': 'joselo24',
    'first': 'jose',
    'last': 'martinez',
    'age': '24',
    'city': 'madrid'
}

new_user = dict(username='joselo24', first='jose', last='martinez', age='24', city='madrid')

#borra las propiedades
#user.clear()

# Elimina una propiedad y nos devuelve el valor de la propiedad
#username = user.pop('username')

# Obtiene el valor de una propiedad
print(user.get('username'))
# Obtiene el valor de una propiedad y si no existe devuelve un valor por defecto
valor_defecto = user.get('country', 'Yeisson colombia')
print(valor_defecto)

values_funcion = user.values

print(values_funcion())
print(user.keys())

# Recorre un diccionario
print(user.items())

print(user)

# MORE INFO
# https://www.w3schools.com/python/python_dictionaries.asp

