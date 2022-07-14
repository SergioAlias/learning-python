"""
Este ejercicio es un sólo programa, aunque se describa por partes:

1. Escribir una función que retorne True si el número que se le pasa como argumento es mayor o igual que cinco y False en el resto de casos.

2. Escribir una función que, usando la que hemos programado antes, acepte un sólo argumento (que será una lista de números) y retorne un número: el número de elementos de esa lista que es mayor o igual que cinco.

PERO

La función no puede usar ningún bucle (nada de for, ni while ni similares).

3. Para finalizar, crear un decorador y aplicarlo a a la función del primer punto de modo que, si el número que se le pasa a la función es un cero, lo reemplace por un siete. Si tiene cualquier otro valor debe dejarlo sin modificar.
"""


def zero_to_seven(func): # El decorador
    def internal(n): # La función interna que cambia los 0 por 7
        if n == 0:
            n = 7
        return func(n)
    return internal

def how_many_ge_five(li): # Función que retorna el número de elementos de la lista mayores o iguales que 5
    return len(list(filter((zero_to_seven(lambda n: n >= 5)), li)))
# Uso filter() para reducir la lista a los que son mayores o iguales que 5 (los Trues), hago una lista con list() y luego cuento sus elementos con len()
# Aplico el decorador zero_to_seven a la función lambda

###### PRUEBA ######
lista = [0, 1, 2, 3, 5, 9] # La función con esta lista debería retornar 3 porque tiene un 0 (o sea, un 7), un 5 y un 9
print(how_many_ge_five(lista))

'''
Al principio, para la función que retorna True si el número es mayor o igual que 5 hice algo así:

def ge_five(n):
    return n >= 5

Pero en el último Meet recordamos las funciones lambda y pensé que sería interesante usarla aquí
Como uso una función lambda, no aplico el decorador con @, sino que lo aplico directamente a la función
'''
