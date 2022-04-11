# ------------ Made by Jesus Lagares Galan

import pandas as pd 
import csv
import matplotlib.pyplot as plt

# ------------ Obtenemos los datos para parsear el CV ------------

headers = [] # Lista para guardar los headers
days = [] # Lista para guardar los días 
vectorCounter = [] # Lista de listas

# Abrimos el archivo para recabar los datos
with open ('AnomaliesReport.csv') as csvfile: # Abrimos el archivo
    
    plots = csv.reader(csvfile , delimiter=',') 
    for row in plots: # Recorremos    
        
        # Obtenemos el nombre de todos los patrones
        if ( ((row[1] in headers) == False) and row[1] != 'patternName' ): # Nos quedamos con todos los PatternName
            headers.append(row[1]) # Lo guardamos en la lista de headers
        
        # Obtenemos los diferentes días de los timestamp 
        day = row[0].split(maxsplit=1)[0] # Hacemos el split del día     
        if ( (day in days) == False and day != 'currentTimestamp'):
                days.append(day)

# Rellenamos la lista de listas de 0
for day in days: 
    auxiliarVector = []
    for header in headers: 
        auxiliarVector.append(0)
    vectorCounter.append(auxiliarVector)


# Abrimos el archivo de nuevo para realizar el conteo de las repeticiones
with open ('AnomaliesReport.csv') as csvfile: # Abrimos el archivo
    plots = csv.reader(csvfile , delimiter=',') 
    for row in plots: # Recorremos    
        externalIndex = 0 
        for day in days: 
            if (row[0].split(maxsplit=1)[0] == day):
                internalIndex = 0 
                for header in headers: 
                    if (row[1] == header):
                        vectorCounter[externalIndex][internalIndex] += 1
                    else: 
                        internalIndex += 1 # Si no es el patron, pasamos al siguiente
            else: 
                externalIndex += 1


# ------------ Parseamos el CV ------------

title = ["Day" , "Pattern Name" , "Counter"] # Cabeceras 

with open ('dataParseada.csv' , 'w') as parse: # Creamos el fichero csv de salida
        
        csv_writer = csv.writer(parse , delimiter = ',') # Asignamos la funcion para escribir en el

        csv_writer.writerow(title) # Escribimos las cabeceras predefinidas

        externalIndex = 0 # 
        for day in days: # Por cada línea del archivo que leemos 
            internalIndex = 0 
            for header in headers: 
                data_writed = [day , header , vectorCounter[externalIndex][internalIndex]] # Creamos la row que será escrita
                csv_writer.writerow(data_writed) # Escribimos los datos requeridos por cada linea
                internalIndex += 1 

            externalIndex += 1
        