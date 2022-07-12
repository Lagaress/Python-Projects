import csv
import names 
import random 

def random_name():
    return names.get_full_name()

def random_number():
    return random.randint(1 , 100)

print([random_name() , random_number()])

