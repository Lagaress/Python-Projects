import csv
import names 
import random
import os.path

def get_random_name():
    return names.get_full_name()

def get_random_number():
    return random.randint(1 , 99)

def get_vector4_random_number():
    return [get_random_number(), get_random_number(), get_random_number() , get_random_number()]

def create_csv():
    headers = ['Full Name','Amazon','Google','Intel','Apple']
    
    with open('data.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        for row in range(100):
            vector_random_number = get_vector4_random_number()
            writer.writerow([get_random_name(),vector_random_number[0],vector_random_number[1],vector_random_number[2],vector_random_number[3]])

def create_csv_if_not_exist():
    if (not os.path.exists('data.csv')):
        create_csv()
    