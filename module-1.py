"""

Vamos a crear un programa que tenga cuatro funciones (suma, resta, multiplica y divide) con exactamente esos nombres. Las funciones deben operar con números y retornar un resultado según lo que se espera de ellas (la suma sumará, la resta restará, etc).

Por ejemplo:

suma(4, 7)
>> 11

resta(3, 2)
>> 1

multiplica(2, 5)
>> 10

divide(6/2)
>> 3

Todas ellas deben disparar una excepción TypeError si se le introduce algún dato no numérico.

Opcionalmente (para nota) la función suma puede admitir una lista de valores y retornar la suma de todos ellos.

No es necesario crear ejeemplos ni que el programa use esas funciones.
"""


def is_number(data):
    if isinstance(data, int) or isinstance(data, float):
        return True
    return False

def suma(*numbers):
    result = 0
    for n in numbers:
        if is_number(number):
            result += number
        else:
            raise TypeError
    return result

def resta(x, y):
    if is_number(x) and is_number(y):
        return x - y
    else:
        raise TypeError

def multiplica(x, y):
    if is_number(x) and is_number(y):
        return x * y
    else:
        raise TypeError

def divide(x, y):
    if is_number(x) and is_number(y):
        return x / y
    else:
        raise TypeError


