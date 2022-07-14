'''
Este es el proyecto final que se pide para este curso. No es ni mucho menos un proyecto difícil ni complejo, pero requiere tener mucho cuidado en los detalles y, sobre todo asegurarse de que se está haciendo bien.
En este proyecto vas a programar un módulo que luego yo usaré en mi programa. Mi programa es éste:

import proyecto_final as pf
fichero = "fichero_de_prueba.csv"
datos = pf.Consumo(fichero)
print("Consumo total diario:")
datos.total_diario()
print("Promedio diario por horas:")
datos.media_horas()
print("Total: {}".format(datos.total))

Nota que, para que funcione, el módulo debe llamarse "proyecto_final" y, al menos, tener una clase que se llame "Consumo" que tenga los métodos "total_diario()" y "media_horas()" y el atributo "total".

Vamos con los detalles:
El archivo adjunto es un ejemplo de registro horario del consumo eléctrico de un supercomputador
(totalmente inventado, he puesto las cifras al azar y ni siquiera sé si son razonables) en formato CSV
(valores separados por comas).
Vas a escribir un módulo para trabajar con datos del tipo de los de ese archivo.
El módulo debe tener una clase “Consumo” que, al instanciarla, acepte como argumento un nombre
de archivo.
Debe abrir ese archivo (gestionando los posibles errores, como que no exista).
Debe leer los datos (NO DEBES programar el sistema que lea los datos desde cero, el módulo "csv" -
o uno similar- te será de gran ayuda).
La clase “Consumo” tendrá un método "total_diario()" para mostrar un resumen del consumo diario
(esto es, una tabla con el consumo total de cada día durante los días de los que conste el archivo) así:
2021-02-09: 5554.0
2021-02-10: 5674.0
2021-02-11: 9532.0
Es decir, una línea para cada día con la suma del consumo de todas las horas de ese día.
El método "media_horas()" debe mostrar un promedio horario (es decir, una tabla con una lista de
horas que indique el consumo medio en esa hora de todos los días que consten en el archivo, de este
modo:
00:00-01:00: 248.0
01:00-02:00: 191.0
02:00-03:00: 190.0
03:00-04:00: 185.0
04:00-05:00: 198.0
05:00-06:00: 204.0
etc

Es decir, en las 00:00-01:00 mostrará la media de todos los días a las 00:00-01:00, y así con todas.
El atributo "total" debe contener el consumo total durante el periodo contenido en el archivo. Es decir,
la suma de todos los consumos de todas las horas de todos los días.
Como resultado de todo esto, al ejecutar mi programa usando el módulo que has creado, la salida
debería mostrar automáticamente algo como esto (pero con los datos correctos):
Consumo total diario:
2021-02-09: 5554.0
2021-02-10: 5554.0
2021-02-11: 5554.0
Promedio diario por horas:
00:00-01:00: 248.0
01:00-02:00: 191.0
02:00-03:00: 190.0
03:00-04:00: 185.0
04:00-05:00: 198.0
etc

Para subir nota se le pueden agregar funcionalidades al código (aunque no se usarán en el programa,
que será exactamente como se ha visto arriba):
Se puede agregar un método o función que, indicándole la fecha de un día concreto, muestre los datos
de esa fecha, si es que existe en el archivo.
Se puede agregar un método o función que muestre el consumo total para un periodo concreto.
En resumen: Se puede añadir cualquier funcionalidad que se te ocurra, como guardar datos a archivo,
dibujar gráficas o lo que sea. pero todo lo que se añada debería estar documentado con comentarios o,
mejor, con docstrings.
'''


import matplotlib.pyplot as plt # Necesario instalar
import csv, sys, os.path

class Consumo():

    def __init__(self, filename):
        self.filename = str(filename) # El atributo con el nombre del fichero
        self.data = [] # La lista que contendrá los datos del fichero
        self.total = 0 # El atributo 'total' empieza en cero
        self.header = [] # Un atributo que guardará la cabecera del csv, por si fuera de interés para el usuario
        try:
            with open(self.filename) as file: # Abro el fichero
                my_csv = csv.reader(file) # Abro el lector de csv y lo asigno a 'my_csv'
                for row in my_csv: # Itero sobre las filas que va leyendo el lector
                    try:
                        self.total += float(row[2]) # Para cada fila del csv, añade el consumo al atributo 'total'
                        self.data.append(row) # Añado la fila como una lista a mi lista 'data', que será una lista de listas.
                    except ValueError: # Este error se dispara cuando el iterador se encuentra con la cabecera del csv (si la hubiese), ya que no puede convertir row[2] en float
                        self.header.append(row) # Me guardo la fila de cabecera por si el usuario la necesitase
                                                # Así se pueden leer ficheros .csv con y sin cabecera
        except FileNotFoundError: # Este error se dispara cuando no encuentra el fichero
            print("El fichero especificado no existe. Por favor, comprueba la ruta o el nombre del fichero que desea utilizar.")
            sys.exit() # Paro el programa
        except (UnicodeDecodeError, IndexError): # Haciendo pruebas vi que cuando el fichero no es .csv o está malformado (por ejemplo, si cambio una coma por un punto y coma) se disparan estos errores
            print("El fichero especificado parece estar malformado. Por favor, revise que se trata de un fichero CSV y que esté construido correctamente.")
            sys.exit()

    def column_names(self, ind):
        '''
        QUÉ HACE: 
        Crea una lista con los nombres de los diferentes elementos de una columna.
        Por ejemplo, si la aplicamos sobre la columna de los días, retornará una lista de este estilo:
        ["2021-02-09", "2021-02-10", "2021-02-11", "2021-02-12", "2021-02-13"]

        CÓMO SE USA:
        El argumento 'ind' es el índice de la columna. Toma los valores 0 (columna de los días) o 1 (columna de las horas)
        Este método no está pensado para usarse directamente, sino que se usa en iteradores de otros métodos más abajo.
        La razón de su existencia es básicamente para ahorrar código.

        MÁS DETALLES: 
        Leer comentarios del cuerpo del método
        '''    
        my_list = []
        if ind != 0 and ind != 1: # Comprueba que se use 0 o 1 como índice, y si no es así termina el programa con un mensajito.
            print("Has especificado un índice no permitido. Utiliza '0' para los días o '1' para las horas.")
            sys.exit()
        for row in self.data: # Bucle que recorre todas las sub-listas ("filas") de la lista de datos
            if row[ind] not in my_list:
                my_list.append(row[ind]) # "Si ese elemento no estaba en la lista, añádelo"
        return my_list

    def total_mean_generator(self, ind, calc_mean):
        '''
        El método más importante del módulo.

        QUÉ HACE: 
        Crea una lista de los valores medios o totales de cada día u hora.

        CÓMO SE USA:
        El argumento 'ind' será 0 si queremos filtrar por días, o 1 si queremos filtrar por horas.
        El argumento 'calc_mean' será True si queremos que retorne una lista de medias, o False si queremos que retorne una lista de valores totales.

        MÁS DETALLES:
        Leer comentarios del cuerpo del método
        '''    
        if calc_mean != True and calc_mean != False: # Compruebo que calc_mean sea True o False
            print("Si quieres los valores totales, especifica 'False'; si quieres los valores medios, especifica 'True'.")
            sys.exit()
        total_list, mean_list = [], [] # Creo dos listas: una que contendrá los valores totales por cada día u hora, y otra que contendrá los valores medios.
        waste = 0 # Aquí se irá guardando el consumo total por día u hora
        total_entries = 0 # Aquí se guardará el total de datos para un día u hora concretos, para poder calcular la media
        for i in self.column_names(ind): # Un bucle que recorre la lista creada por column_names(). Por ejemplo, si 'ind' es 0 el bucle haría algo como "Por cada día que hay en la lista de días..."
            for row in self.data: # Recorro las sub-listas ("filas") de mi lista 'data'
                if i == row[ind]: # "Si el día/hora de esa fila coincide con el día/hora con el que estoy iterando:"
                    waste += float(row[2]) # "... añade el valor del consumo de esa fila a 'waste'... "
                    total_entries += 1 # "... y añade 1 a la lista del total de datos."
            # Cuando termino de iterar en todas las filas de datos:
            total_list.append([i, waste]) # Añado a la lista de totales el día/hora junto a su consumo total
            mean_list.append([i, waste/total_entries]) # Añado a la lista de medias el día/hora junto a su consumo medio
            waste = 0 # Lo vuelvo a poner a 0 para que itere con el siguiente día/hora de mi lista de días/horas
            total_entries = 0 # Lo mismo con esta variable
        if calc_mean: # "Si quieres los valores medios..."
            return mean_list # "... retorna la lista de los valores medios"
        else: 
            return total_list # "Si no, retorna la de los valores totales"

    def total_diario(self):
        '''
        QUÉ HACE: 
        Imprime el consumo total de cada día.
        '''  
        for i in self.total_mean_generator(0, False): # Especificamos 0 para que filtre por días y False para obtener los valores totales
            print(f"{i[0]}: {i[1]}") # Lo imprime en el formato especificado en el ejercicio


    def media_horas(self):
        '''
        QUÉ HACE: 
        Imprime el consumo medio de cada hora.
        '''  
        for i in self.total_mean_generator(1, True): # 1 para que filtre por horas, True para obtener los valores medios
            print(f"{i[0]}: {i[1]}")
        
    ######  FUNCIONALIDADES EXTRA  ######

    # Aprovechando que tengo un método general para totales y medias, he implementado los otros dos métodos que pueden hacerse:

    def media_diaria(self):
        '''
        QUÉ HACE: 
        Imprime el consumo medio de cada día.
        ''' 
        for i in self.total_mean_generator(0, True): # 0 para que filtre por días, True para obtener los valores medios
            print(f"{i[0]}: {i[1]}")

    def total_horas(self):
        '''
        QUÉ HACE: 
        Imprime el consumo total de cada hora.
        ''' 
        for i in self.total_mean_generator(1, False): # 1 para que filtre por horas, False para obtener los valores totales
            print(f"{i[0]}: {i[1]}")

    ###### FILTRADO DE DATOS ######

    def column_items_filter(self, ind, first_item, last_item = None):
        '''
        QUÉ HACE: 
        Filtra la lista generada por column_names(). Puede filtrarse un día/hora concreto, o un rango continuo.

        CÓMO SE USA:
        El argumento 'ind' es 0 si filtramos por días o 1 si filtramos por horas.
        El arguento 'first_item' es el día/hora concreto que queremos filtrar.
        Opcionalmente, para filtrar un rango de días/horas, se especifica el argumento 'last_item'.
        Este método se usa en otros métodos más abajo.

        MÁS DETALLES:
        Leer comentarios del cuerpo del método
        '''
        try:
            if last_item == None: # Si no se especifica last_item, toma el valor de first_item, y así en vez de un rango se filtra por ese día/hora en cocnreto
                last_item = first_item
            full_list = self.column_names(ind) # Le damos nombre a nuestra lista generada por column_names(), por comodidad
            filtered_list = [] # La lista que contendrá los días/horas filtrados
            first_index = full_list.index(first_item) # Le doy nombre al índice del día/hora que quiero filtrar
            last_index = full_list.index(last_item) # Lo mismo pero con el índice de 'last_item'
            for i in full_list: # Recorro la lista completa de días/horas
                if first_index <= full_list.index(i) <= last_index: # "Si el día/hora entra dentro del rango que quiero filtrar..."
                    filtered_list.append(i) # "... añádelo a la lista de filtrados"
            return filtered_list # Retorna la nueva lista filtrada
        except ValueError: # Si se especifica un día/hora que no está en el fichero, se genera un ValueError que capturo aquí
            print("Estás intentando filtrar por un día/hora que no existe en el fichero. Comprueba que esté bien escrito.")
            sys.exit()

    def filtered_data_generator(self, ind, first_item, last_item = None):
        '''
        QUÉ HACE: 
        Filtra la lista de datos del fichero. Puede filtrarse un día/hora concreto, o un rango continuo.

        CÓMO SE USA:
        El argumento 'ind' es 0 si filtramos por días o 1 si flitramos por horas.
        El arguento 'first_item' es el día/hora concreto que queremos filtrar.
        Opcionalmente, para filtrar un rango de días/horas, se especifica el argumento 'last_item'.
        Este método puede usarse para crear una lista que luego se exporte como csv con otro método creado para ello más abajo

        MÁS DETALLES:
        Leer comentarios del cuerpo del método
        '''
        filtered_data_list = [] # La nueva lista de datos filtrados
        for row in self.data: # Recorremos nuestra lista de datos
            if row[ind] in self.column_items_filter(ind, first_item, last_item): # "Si el día/hora de la fila de la lista de datos está en la lista de días/horas filtrada..."
                filtered_data_list.append(row) # "... añade la fila a la lista de datos filtrados"
        return filtered_data_list

    def filtered_total_mean_generator(self, ind, calc_mean, first_item, last_item = None):
        '''
        QUÉ HACE: 
        Crea una lista de los valores medios o totales de cada día u hora, filtrado por un día/hora o un rango de días/horas.
        Básicamente actúa sobre total_mean_generator() y filtra el día/hora o rango de días/horas que seleccionemos.

        CÓMO SE USA:
        El argumento 'ind' será 0 si queremos filtrar por días, o 1 si queremos filtrar por horas.
        El argumento 'calc_mean' será True si queremos que retorne una lista de medias, o False si queremos que retorne una lista de valores totales.
        El arguento 'first_item' es el día/hora concreto que queremos filtrar.
        Opcionalmente, para filtrar un rango de días/horas, se especifica el argumento 'last_item'.
        Este método se utilizará en otros métodos más abajo, pero también se puede usar para filtrar datos que luego se guarden como csv.

        MÁS DETALLES:
        Leer comentarios del cuerpo del método
        '''
        filtered_total_mean_list = [] # La nueva lista de totales/medias filtrada
        for i in self.total_mean_generator(ind, calc_mean): # Itera sobre la lista que retorna total_mean_generator()
            if i[0] in self.column_items_filter(ind, first_item, last_item): # "Si el día/hora de la fila está en la lista de días/horas filtrada..."
                filtered_total_mean_list.append(i) # " ... añádela a esta nueva lista"
        return filtered_total_mean_list

    ###### MÉTODOS DE TOTALES Y MEDIAS FILTRADOS ######
    # La versión de los cuatro métodos anteriores de totales y medias, pero en una versión que admiten filtrar datos

    def filtered_total_diario(self, first_item, last_item = None):
        '''
        QUÉ HACE: 
        Imprime el consumo total de un día o rango de días.

        CÓMO SE USA:
        El arguento 'first_item' es el día concreto que queremos filtrar.
        Opcionalmente, para filtrar un rango de días, se especifica el argumento 'last_item'.        
        ''' 
        for i in self.filtered_total_mean_generator(0, False, first_item, last_item): # 0 para filtrar por días, False para valores totales
            print(f"{i[0]}: {i[1]}")

    def filtered_media_horas(self, first_item, last_item = None):
        '''
        QUÉ HACE: 
        Imprime el consumo medio de una hora o rango de horas.

        CÓMO SE USA:
        El arguento 'first_item' es la hora concreta que queremos filtrar.
        Opcionalmente, para filtrar un rango de horas, se especifica el argumento 'last_item'.        
        ''' 
        for i in self.filtered_total_mean_generator(1, True, first_item, last_item): # 1 para filtrar por horas, True para valores medios
            print(f"{i[0]}: {i[1]}")
        
    def filtered_media_diaria(self, first_item, last_item = None):
        '''
        QUÉ HACE: 
        Imprime el consumo medio de un día o rango de días.

        CÓMO SE USA:
        El arguento 'first_item' es el día concreto que queremos filtrar.
        Opcionalmente, para filtrar un rango de días, se especifica el argumento 'last_item'.        
        ''' 
        for i in self.filtered_total_mean_generator(0, True, first_item, last_item): # 0 para filtrar por días, True para valores medios
            print(f"{i[0]}: {i[1]}")

    def filtered_total_horas(self, first_item, last_item = None):
        '''
        QUÉ HACE: 
        Imprime el consumo total de una hora o rango de horas.

        CÓMO SE USA:
        El arguento 'first_item' es la hora concreta que queremos filtrar.
        Opcionalmente, para filtrar un rango de horas, se especifica el argumento 'last_item'.        
        ''' 
        for i in self.filtered_total_mean_generator(1, False, first_item, last_item): # 1 para filtrar por horas, False para valores totales
            print(f"{i[0]}: {i[1]}")

    ###### MÉTODOS DE CREACIÓN ######

    # Métodos para crear diferentes cosas

    def create_csv(self, data, headers, file_name = "filtered_data.csv"):
        '''
        QUÉ HACE: 
        Crea un fichero csv a partir de una lista de datos

        CÓMO SE USA:
        El argumento 'data' es una lista de datos. Podemos obtener esa lista con cualquiera de los métodos que acaban en _generator, a saber:
         - total_mean_generator()
         - filtered_data_generator()
         - filtered_total_mean_generator()
        Es decir, podremos crear csv con valores medios o totales, filtrando algunos días/horas, o haciendo ambas cosas.
        El argumento 'headers' será una lista con los nombres que queremos que tenga cada columna. Por ejemplo, si tenemos datos de consumo medio por día la lista será algo como ["Día", "Consumo medio"]
        El arguento 'file_name' es el nombre que le pondremos al fichero.

        MÁS DETALLES:
        Leer comentarios del cuerpo del método
        '''
        if not isinstance(data, list): # Compruebo que 'data' sea una lista
            print("Los datos introducidos no están en forma de lista. Por favor, considera utilizar alguno de los métodos acabados en '_generator' para obtener tu lista de datos.")
            sys.exit()
        if not isinstance(headers, list): # Compruebo que 'headers' sea una lista
            print("Los nombres de la cabecera deben estar en forma de lista. Consulta la documentación del método para ver un ejemplo.")
            sys.exit()
        if len(headers) != len(data[0]): # Compruebo que haya exactamente un header por columna de datos
            print("Por favor, pon el mismo número de nombres de cabecera que de columnas. Consulta la documentación del método para ver un ejemplo.")
            sys.exit()
        if file_name[-4:] != ".csv": # Compruebo que el nombre del fichero a crear tenga extensión .csv
            print("Por favor, especifica un nombre de fichero con extensión .csv")
            sys.exit()
        header_list = [headers] # Meto la lista de headers en otra lista para que el csv.writer no explote. Si le paso directamente algo como ["Día", "Consumo medio"], me escribe en el csv: D,í,a C,o,n,s,u,m,o, ,m,e,d,i,o. Para evitar que haga eso meto la lista en otra lista, y así escribe bien el header (Día,Consumo medio)
        while os.path.isfile(file_name): # Un bucle para que no sobreescriba ficheros existentes. Si el nombre del fichero ya existe, le añade '_bis' al nombre. Si sigue existiendo, le añade otro '_bis'. Y así hasta que no exista
            file_name = file_name.replace(".csv", "_bis.csv")
        new_file = open(file_name, "w") # Abro el fichero nuevo
        with new_file:
            nf_writer = csv.writer(new_file, lineterminator='\n') # Abro el csv.writer (le especifico el lineterminator porque si no me escribía una línea vacía entre línea y línea)
            nf_writer.writerows(header_list) # Añado los headers
            nf_writer.writerows(data) # Añado los datos

    def create_plot(self):
        '''
        QUÉ HACE: 
        Grafica los datos.

        CÓMO SE USA:
        Simplemente se llama y listo.

        MÁS DETALLES:
        Leer comentarios del cuerpo del método
        '''
        y_axis, x_axis = [], [] # Creo dos listas para los ejes X e Y

        with open(self.filename) as file: # Abro el csv
            my_csv= csv.reader(file) # Lo leo
            for row in my_csv: # Itero sobre sus filas
                try:
                    y_axis.append(float(row[-1])) # Añado a la lista del eje Y el valor del consumo
                    x_axis.append(row[0][8:] + " " + row[1][0:2] + "-" + row[1][6:8]) # Añado al eje X una cadena de texto con formato "09 00-01" (día hora:hora)
                except ValueError: # Cuando el reader intenta hacer lo anterior con los headers, genera este error y aquí lo capturo
                    x_label = str(row[0]) # Añado el header de la columna de los días ('Fecha') a x_label
                    y_label = str(row[-1]) # Añado el header de la columna de consumo ('Consumo') a y_label
        plt.plot(x_axis, y_axis, lw = 2, c = "g", marker = "o", ms = 5, mfc = "g") # Creo el gráfico con especificaciones sobre el color del gráfico, el tamaño de la línea y de los puntos, etc
        plt.title(self.filename[:-4]) # El título del gráfico será el nombre del fichero sin la extensión .csv
        plt.xlabel(x_label) # Añado el x_label al gráfico
        plt.ylabel(y_label) # Añado el y_label al gráfico
        plt.xticks(rotation = 45) # Roto un poco las etiquetas del eje X, que si no no se lee bien ni cuando haces zoom
        plt.tick_params(axis = "x", labelsize=7) # Le bajo el tamaño a las etiquetas del eje X para que quepan mejor
        plt.show() # Se muestra el gráfico en una ventana


    def create_bill(self, fixed_part = 25.0, variable_part = 0.02):
        '''
        QUÉ HACE: 
        Imprime una factura por el consumo eléctrico del supercomputador. No sirve para mucho pero queda chulo.

        CÓMO SE USA:
        Simplemente se llama y listo. Si se desea, hay argumentos opcionales para cambiar la tasa fija por día y el precio por unidad de energía (yo me los he inventado descaradamente)

        MÁS DETALLES:
        Leer comentarios del cuerpo del método
        '''
        if not isinstance(fixed_part, float) or not isinstance(variable_part, float): # Compruebo que los precios sean números
            print("Los precios deben ir en formato decimal. Si quieres poner un número entero, añade '.0' al final.")
            sys.exit()
        # Imprimo la factura, haciendo las cuentas para calcular los gastos fijos por día, por unidad de energía y el IVA
        print(f'''
 ____________________________________________________________
|                                                            |
                                                            
      █▀▀ ▄▀█ █▄▀ █▀▀ █▄ █ █▀▄ █▀▀ █▀ ▄▀█     █▀   █         
      █▀  █▀█ █ █ ██▄ █ ▀█ █▄▀ ██▄ ▄█ █▀█ █   ▄█ ▄ █▄▄ ▄                                                             
                                                            
      "Promoviendo energías no renovables deesde 1995"       
           Domicilio social: C/ Wallaby 42, Sydney            
                                                             
       Suministros de energía para supercomputadores         
                                                             
    Factura    Número    Pág.   Fecha        Cliente         
               000582     1     28/03/2021   Sergio Alías  
                                                             
                                                             
    Descripción       Cantidad  Precio Ud.  Subtotal         
    -----------       --------  ----------  --------         
    Tasa fija diaria  {len(self.column_names(0))}         {fixed_part} EUR    {len(self.column_names(0))*fixed_part} EUR          
                                                             
    Consumo total     {self.total}   {variable_part} EUR    {round(self.total*variable_part, 2)} EUR       
    _________________________________________________        
                                            {round(len(self.column_names(0))*fixed_part+self.total*variable_part, 2)} EUR      

    Impuestos:

    Tipo    Base imponible     IVA
    -----   ---------------    ------     
    21,00   {round(len(self.column_names(0))*fixed_part+self.total*variable_part, 2)}            {round((len(self.column_names(0))*fixed_part+self.total*variable_part)*0.21, 2)}

    -------------------------------  TOTAL: {round((len(self.column_names(0))*fixed_part+self.total*variable_part)*1.21, 2)} EUR

    
    Aviso legal: Le informamos de que de bla bla bla...

    Gracias por confiar en nosotros

    Fakendesa, S.L.

|____________________________________________________________|
''')
