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
            companies[company_column-1].append(row)

        flag = ( (len(amazon) == 25) and (len(google) == 25) and (len(intel) == 25) and (len(apple) == 25))
        while (not flag):
            counter = 1
            for company in companies: 
                order_array(company, counter)
                counter += 1 
                while len(company) > 25:
                    auxiliar_element = company.pop()
                    auxiliar_element_values_array = [auxiliar_element[1],auxiliar_element[2],auxiliar_element[3],auxiliar_element[4]]
                    auxiliar_element[get_max_in_vector(auxiliar_element_values_array)] = 0
                    auxiliar_element_values_array = [auxiliar_element[1],auxiliar_element[2],auxiliar_element[3],auxiliar_element[4]]
                    company_column = get_max_in_vector(auxiliar_element_values_array)
                    companies[company_column-1].append(auxiliar_element)

            flag = ( (len(amazon) == 25) and (len(google) == 25) and (len(intel) == 25) and (len(apple) == 25))

        create_output_csv(companies)

def create_output_csv(initial_array):
    headers = ['Amazon','Google','Intel','Apple']
    
    with open('output.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        for iterator in range(len(initial_array[0])):
            amazon_element = str(initial_array[0][iterator][0])+" ("+str(initial_array[0][iterator][1])+")"
            google_element = str(initial_array[1][iterator][0])+" ("+str(initial_array[1][iterator][2])+")"
            intel_element = str(initial_array[2][iterator][0])+" ("+str(initial_array[2][iterator][3])+")"
            apple_element = str(initial_array[3][iterator][0])+" ("+str(initial_array[3][iterator][4])+")"

            row = [amazon_element,google_element,intel_element,apple_element]

            writer.writerow(row)



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

