# ------------ Made by Jesus Lagares Galan

import pandas as pd 
import csv
import matplotlib.pyplot as plt

# ------------ Obtenemos el conteo de patrones ------------

headers = [] # Lista para guardar los headers
numericData = [] # Lista de listas

with open ('AnomaliesReport.csv') as csvfile: # Abrimos el archivo
    plots = csv.reader(csvfile , delimiter=',') 
    for row in plots: # Recorremos
        
        if ( ((row[1] in headers) == False) and row[1] != 'patternName' ): # Nos quedamos con todos los PatternName
            headers.append(row[1]) # Lo guardamos en la lista de headers
            numericData.append(0) # Inicializamos la lista con 0. Mismo numero de elementos como patrones tengamos 

        index = 0 # Reiniciamos el index 
        for header in headers: # Recorremos los diferentes patrones
            if (row[1] == header):
                numericData[index] += 1 # Contamos instancias de los eventos
            else:
                index += 1 # Si no es el patron, pasamos al siguiente
        
    print(headers)
    print(numericData)

# ------------ Pintamos ------------
plt.bar(headers, numericData, color=['r', 'b', 'g', 'y', 'black']) # Seleccionamos el estilo de barra con diferentes colore y variables
plt.xlabel('Pattern Name') # Etiqueta dle eje de abcisas
plt.ylabel('Pattern Frecuency') # Etiqueta del eje de ordenadas
plt.title('Pattern Count') # Titulo de la tabla 
plt.show() 