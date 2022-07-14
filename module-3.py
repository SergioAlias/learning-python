"""
la sucesión de Fibonacci es una sucesión infinita de números naturales. 

Comienza con el número 0 seguido del 1. a partir de ahí, el siguiente número de la sucesión se calcula sumando los dos inmediatamente anteriores.

por lo tanto, el tercer número sería 1 (0 + 1), el cuarto sería 2 (1 + 1), el quinto sería 3 (1 + 2), etc.

De este modo, los diez primeros números de la sucesión son los siguientes.

0
1
1
2
3
5
8
13
21
34


El ejercicio de esta semana consiste en crear un programa que muestre los primeros 50 números de la sucesión de Fibonacci.

para ello se deberá usar alguno de los métodos vistos en el tema de esta semana.

Para nota:

Crear para este programa una clase que se pueda instanciar indicando el número de dígitos que queremos de este modo:

sucesion = Fibonacci(5)

Que tenga un método "list" que muestre todos los números hasta el indicado:

sucesion.list()

0
1
1
2
3


Que, al imprimir nuestro objeto, muestre el último de ellos:

print(sucesion)

3

"""


# Para crear el método que genera la sucesión en sí, usaré la sentencia yield vista en el temario

class Fibonacci():

    def __init__(self, length):
        self.length = length # El número de elementos de la sucesión

    def create_fib(self): # La funcón generadora de la sucesión
        current, queue = 0, 1 # Meto el primer y segundo número de la sucesión
        for i in range(self.length): # Bucle que se repite según el número de elementos de la sucesión que queramos
            yield current # Genera el primer elemento de la sucesión
            current, queue = queue, current + queue # El segundo elemento avanza de la cola (queue) a la primera posición (current), y se genera el tercer elemento en la cola (queue)

    def list(self):
        for i in self.create_fib():
            print(i) # Muestra todos los elementos de la sucesión

    def __str__(self): # Método __str__() programado para que, al imprimir el objeto, muestre el último elemento de la sucesión
        last_item = "No hay elementos en esta sucesión" # Variable para ir guardando lo que retorna el generador. Tiene un mensaje por defecto por si acaso se instancia una sucesión sin elementos -> Fibonacci(0)
        for i in self.create_fib():
            last_item = i # Este bucle va guardando el retorno del generador, y al final se queda con el último elemento
        return str(last_item) # Retorna el último elemento de la sucesión convertido en cadena de texto

####### PROGRAMA DE PRUEBA #######

sucesion = Fibonacci(50) # Instanciamos un objeto que contendrá 50 elementos de la sucesión

sucesion.list() # Mostramos todos los elementos

print("Último elemento de la sucesión:")
print(sucesion) # Al imprimir el objeto, muestra el último elemento
