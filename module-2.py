"""
Vamos a crear un pequeño programa con un par de clases para gestionar una biblioteca.

La primera de estas clases será la clase "Libro", que servirá para describir cada libro de nuestra biblioteca.
La segunda clase será "Biblioteca", que describirá la biblioteca en sí.

"Libro" debe ser una clase con los siguientes atributos:
    Título
    Autor

Deberá ser posible asignarle valores a loa atributos del libro al instanciarlo de este modo:

mi_libro = Libro("Título del libro", "Nombre del Autor")

"Biblioteca" es una clase que debe poder contener una lista de libros, y debería poder crearse sin necesidad de argumentos:

mi_biblioteca = Biblioteca

Deben poder agregarse libros con un método "add" de este modo:

mi_biblioteca.add(mi_libro)

Deberá poderse mostrar una lista de los libros que contiene la biblioteca de este modo:

mi_biblioteca.show()

Lo que debería mostrar una lista del estilo de la siguiente:

Título del libro 1 (Nombre del Autor 1)
Título del libro 2 (Nombre del Autor 2)
Título del libro 3 (Nombre del Autor 3)

Para nota:

Que la biblioteca guarde la información de estado de cada libro (si está disponible o está prestado).
Que tenga sendos métodos para prestar y retornar un libro determinado (nota que para esto debe existir un modo de referirse al libro).
Que, al mostrar el listado de libros, indique si está disponible o no.

El programa que hagamos usará estos objetos para hacer lo siguiente automáticamente:

1: Crear una biblioteca.
2: Añadir tres libros a esa biblioteca.
3: Mostrar la lista de libros.

Si Se ha añadido un sistema de préstamos de libros, se deberá continuar de este modo:

4: Prestar un libro.
5: Volver a mostrar la lista de libros.
4: Retornar el libro prestado.
5: Volver a mostrar la lista de libros una última vez.
"""


####### DEFINICIÓN DE LAS CLASES #######

class Libro():
    def __init__(self, titulo, autor): # Aquí declaro los atributos de la clase Libro
        self.titulo = titulo
        self.autor = autor

class Biblioteca():
    def __init__(self):
        self.lista_de_libros = [] # La lista de libros empieza vacía
        self.lista_disponible = [] # La lista de disponibilidades empieza vacía

    def add(self, libro): # Método para añadir libros a la biblioteca
        if isinstance(libro, Libro): # Compruebo que lo que intentan añadir sea un libro de la clase Libro
            self.lista_de_libros.append(libro) # Añado el libro a la lista
            self.lista_disponible.append(True) # Añado la disponibilidad del libro a la lista (por defecto True), indexada en la misma posición que el libro en su lista
            # Esta parte al principio la hice simplemente añadiendo un atributo al libro con "libro.disponible = True", pero me di cuenta de que [...]
            # [...] si lo hacía así y luego creaba más de una biblioteca no podría poner un mismo libro disponible en una y prestado en otra.
            print(f"Se ha añadido a la biblioteca el libro {libro.titulo}, de {libro.autor}.") # Mensajito de confirmación
            print() # Para que me deje una línea libre, que si no lo veo todo muy pegado. Espero que esto no sea una mala práctica

    def show(self): # Método para mostrar la lista de libros de la biblioteca
        print("LISTA DE LIBROS DE LA BIBLIOTECA")
        libros_disponibles = 0 # Esta variable la uso para que el método no me imprima el titulito de "Disponibles:" si resulta que no hay libros disponibles
        libros_prestados = 0 # Lo mismo pero para el titulito de "Prestados:"
        for libro in self.lista_de_libros: # Un bucle que recorre la lista de libros
            if self.lista_disponible[self.lista_de_libros.index(libro)]: # Consulto en la lista de disponibilidades, en la misma posición del libro en su lista de libros
                libros_disponibles += 1 # La variable guarda el número de libros disponibles
        if libros_disponibles > 0: # Si hay libros disponibles, mostrará el título "Disponibles:"
            print("Disponibles:")
        for libro in self.lista_de_libros: # Otro bucle para recorrer la lista de libros
            if self.lista_disponible[self.lista_de_libros.index(libro)]: # "Si el libro está disponible:"
                print(f"- {libro.titulo} ({libro.autor})") # Muestro los libros disponibles, si los hubiera
        for libro in self.lista_de_libros:
            if not self.lista_disponible[self.lista_de_libros.index(libro)]:
                libros_prestados += 1 # Esta variable me guarda el número de libros prestados
        if libros_prestados > 0:
            print("Prestados:") # Así, si no hay libros prestados, no me muestra el titulito "Prestados:". No tiene sentido mostrarlo si después no se muestra ningún libro   
        for libro in self.lista_de_libros:
            if not self.lista_disponible[self.lista_de_libros.index(libro)]: # "Si el libro no está disponible:"
                print(f"- {libro.titulo} ({libro.autor})") # Muestro los libros prestados, si los hubiera
        print() # Dejo una línea vacía para espaciar        

    def prestar(self, libro): # Método para prestar libros
        if self.lista_disponible[self.lista_de_libros.index(libro)]: # "Si el libro está disponible:"
            self.lista_disponible[self.lista_de_libros.index(libro)] = False # Cambio la disponibilidad del libro que se quiere prestar a False
            print(f"Se ha prestado el libro {libro.titulo}, de {libro.autor}.") # Mensajito de confirmación
            print() # Dejo una línea vacía para espaciar
        else:
            print("El libro no está disponible en este momento.") # Por si se intenta prestar un libro ya prestado

    def retornar(self, libro): # Método para retornar libros
        if not self.lista_disponible[self.lista_de_libros.index(libro)]: # "Si el libro no está disponible:"
            self.lista_disponible[self.lista_de_libros.index(libro)] = True # Cambio la disponibilidad del libro retornado a True
            print(f"Se ha devuelto el libro {libro.titulo}, de {libro.autor}.") # Mensajito de confirmación
            print()
        else:
            print("Este libro ya está en la biblioteca.") # Por si se intenta retornar un libro que está disponible


####### PROGRAMA #######

libro_1 = Libro("El gen egoísta", "Richard Dawkins")
libro_2 = Libro("La niebla", "Stephen King")
libro_3 = Libro("Shingeki no Kyojin Vol. 20", "Hajime Isayama") # Creo tres objetos del tipo Libro

mi_biblioteca = Biblioteca() # Creo la biblioteca

for i in range(3):
    mi_biblioteca.add([libro_1, libro_2, libro_3][i]) # Añado los tres libros a la biblioteca, de una sola vez para ahorrar código

mi_biblioteca.show() # Muestro la lista inicial de libros

mi_biblioteca.prestar(libro_2) # Presto el segundo libro

mi_biblioteca.show() # Muestro la lista otra vez

mi_biblioteca.retornar(libro_2) # Retorno el libro prestado

mi_biblioteca.show() # Muestro la lista una última vez
