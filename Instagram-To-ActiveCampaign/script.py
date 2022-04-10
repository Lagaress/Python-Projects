# Incluimos las librerías a utilizar
from instascrape import *
import csv
from random import seed, randint

# Creamos el vector de las cabeceras del csv
titles = ["Email Address" , "Name" , "Instagram" , "Category"]
tratosTitles = [ "Conductos" , "Identificador de conducto" , "Etapa" , "Titulo" , "Nombre de usuario de propietario de trato" , "Email de propietario" , "ID de usuario de propietario de trato" , "Email de Contacto" ]

# Cookie de inicio de sesión para evitar la pantalla de login
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
    "cookie": "sessionid=40481132764%3AT8QuHRGtm8jPZz%3A27;"
}

archivoDeTexto = open("profiles.txt" , "r") # Abrimos el fichero de entrada

# Creamos el archivo de salida para los Contactos
with open ('profiles.csv' , 'w') as new_file: # Creamos el fichero csv de salida

    csv_writer = csv.writer(new_file , delimiter = ',') # Asignamos la funcion para escribir en el

    csv_writer.writerow(titles) # Escribimos las cabeceras predefinidas


    for line in archivoDeTexto: # Accedemos a cada línea del archivo

        user = Profile(line) # Accedemos a 
        user.scrape(headers=headers) # Le pasamos la cookie con el id de inicio de sesión

        userFollowers = user.followers # Obtenemos el número de usuarios

        # Generamos el email aleatorio
        randomEmail = "noEmail" + str(randint(0 , 10000)) + "@gmail.com" # Utilizamos noEmail + Numero Aleatorio

        # Hacemos la distinción en función del número de embajadores
        if ( userFollowers > 25000 ):

            category = "Advisor" 

        elif ( userFollowers > 5000 and userFollowers < 25000 ):

            category = "Ambassador"   

        else: 

            category = "Micro"

        # Información a escribir en la fila del csv
        data_writed = [ randomEmail , user.full_name  , user.username , category]  # Definimos los datos requeridos por truspilot

        # Escribimos la información
        csv_writer.writerow(data_writed) 



# Creamos el archivo de salida para los Tratos [LAS OPCIONES PODRÍAN SER PERSONALIZABLES EN UN FUTURO]
with open ('profiles.csv' , 'r', encoding="ISO-8859-1") as csv_file: # Abrimos el dataset para leer los datos

    csv_reader = csv.reader(csv_file) # Asignamos la funcion para leer
    
    with open ('tratos.csv' , 'w' , encoding="ISO-8859-1") as new_file: # Creamos el fichero csv de salida
        
        csv_tratos = csv.writer(new_file , delimiter = ',') # Asignamos la funcion para escribir en el

        csv_tratos.writerow(tratosTitles) # Escribimos las cabeceras predefinidas

        csv_reader.__next__() # Nos saltamos la primera línea del archivo => La correspondiente a los headers del archivo leído

        for line in csv_reader: # Por cada línea del archivo que leemos 
    
            data_writed = [ "Alvarolb" , 8 , "To Contact" , line[1]+" "+"["+line[3]+"]" , "Alvaro Lafuente" , "alvaro@pentalium.com" , 3 , line[0]]  # Definimos los datos requeridos por truspilot

            csv_tratos.writerow(data_writed) # Escribimos los datos requeridos por cada linea

