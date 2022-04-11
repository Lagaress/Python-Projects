# ------------ Made by Jesus Lagares Galan

import pandas as pd 
import csv
import matplotlib.pyplot as plt

# ------------ Obtenemos el conteo de patrones ------------

markers = [ "." , "v" , "8" , "s" , "p" , "P" , "*" , "X" , "D" , "d" ] # Lista con diversos markers para elegir
headers = [] # Lista para contener el nombre de los patrones
dataContainer = [] # Lista de listas para guardar el número de patrones junto a su día y repeticiones. Su estructura será 1 lista por patrón, 
                        #y 2 listas dentro de cada patrón para guardar el día y la frecuencia

with open ('dataParseada.csv') as csvfile: # Abrimos el archivo
    plots = csv.reader(csvfile , delimiter=',') 
    plots.__next__() # Nos saltamos la primera línea del archivo correspondiente a los headers del CSV
    for row in plots: # Recorremos
        if ( ((row[1] in headers) == False) and row[1] != 'patternName' ): # Nos quedamos con todos los PatternName
            headers.append(row[1]) # Lo guardamos en la lista de headers
            auxiliarList = [] # Creamos una lista auxiliar vacía
            auxiliarIterator = 0 # Creamos un iterador para hacer 2 iteraciones y rellenar con dos listas vacías
            while auxiliarIterator < 2:
                auxiliarList.append([])
                auxiliarIterator += 1
            dataContainer.append(auxiliarList) # Rellenamos la lista vacía, con sus 2 listas vacías dentro, por cada patrón que tengamos almacenado en header
        
        index = 0 # Creamos un index auxiliar
        for header in headers: # Recorremos los diferentes patrones
            if (row[1] == header):
                dataContainer[index][0].append(row[0]) # Añadimos el día
                dataContainer[index][1].append(int(row[2])) # Añadimos el número correspondiente a las repeticiones
                                                # Hacemos un casting a enteros para mejorar la visibilidad en la posterior gráfica
            else:
                index += 1 # Si no es el patron, pasamos al siguiente


# ------------ Pintamos ------------

index = 0 # Reiniciamos el index
for header in headers:
    plt.plot(dataContainer[index][0], dataContainer[index][1] , marker = markers[index] , label=header) # Seleccionamos el estilo de barra con diferentes colore y variables
    index += 1
plt.xlabel('Day') # Etiqueta dle eje de abcisas
plt.ylabel('Pattern Frequency') # Etiqueta del eje de ordenadas
plt.title('Pattern Counting Frequency') # Titulo de la tabla
plt.gcf().autofmt_xdate() # Instrucción para aumentar la legibilidad de las fechas (las pondrá en diagonal)
plt.legend() # Imprimimos la leyenda
plt.show() # Mostramos la gráfica