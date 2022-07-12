import csv

# Amazon[1],Google[2],Intel[3],Apple[4]

def distribute_people_in_companies():

    amazon = []
    google = []
    intel = []
    apple = []
    companies = [amazon,google,intel,apple]

    with open('data.csv','r') as csvfile:   
        csvreader = csv.reader(csvfile)     
        next(csvreader)
        for row in csvreader:
            scores_array = [row[1],row[2],row[3],row[4]]
            company_column = get_max_in_vector(scores_array)
            companies[company_column-1].append(row) # Entra en la lista

    order_array(amazon, 1)
    print(amazon)

def order_array(arr, element_number):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][element_number] < arr[j + 1][element_number]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        if not swapped:
            return


def get_max_in_vector(scores_array):
    max_value = 0
    interaction_counter = 1
    element_counter = 1
    for score in scores_array:
        if (int(score) >= int(max_value)):
            max_value = score
            element_counter = interaction_counter
        interaction_counter += 1
    return element_counter

