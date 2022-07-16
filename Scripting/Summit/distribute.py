import csv

def distribute_people_in_companies():
    try:
        make_distribution()
        
    except Exception as e: 
        print("There was an exception during execution: "+e)    

def make_distribution():
    companies = [[],[],[],[]]

    with open('data.csv','r') as csvfile:   
        csvreader = csv.reader(csvfile)     
        next(csvreader)
        fill_companies_array(csvreader,companies)
        rebalance_arrays(companies)
        create_output_csv(companies)


def fill_companies_array(csvreader,companies):
    for row in csvreader:
        scores_array = [row[1],row[2],row[3],row[4]]
        company_column = get_index_max_element_in_vector(scores_array)
        companies[company_column-1].append(row)

def are_all_arrays_full(companies):
    return ((len(companies[0]) == 25) and (len(companies[1]) == 25) and (len(companies[2]) == 25) and (len(companies[3]) == 25))

def rebalance_arrays(companies):
    while (not are_all_arrays_full(companies)):
        counter = 1
        sort_companies(companies, counter)

def sort_companies(companies, counter):
    for company in companies: 
        order_array(company, counter)
        counter += 1 
        reorder_people_in_companies(companies, company)

def reorder_people_in_companies(companies, company):
    while len(company) > 25:
        last_element = company.pop()
        last_element_values_array = [last_element[1],last_element[2],last_element[3],last_element[4]]
        last_element[get_index_max_element_in_vector(last_element_values_array)] = 0
        last_element_values_array = [last_element[1],last_element[2],last_element[3],last_element[4]]
        company_column = get_index_max_element_in_vector(last_element_values_array)
        companies[company_column-1].append(last_element)


def create_output_csv(initial_array):
    with open('output.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        write_headers_output_csv(writer)
        write_rows_output_csv(initial_array, writer)

def write_headers_output_csv(writer):
    headers = ['Amazon','Google','Intel','Apple']
    writer.writerow(headers)

def write_rows_output_csv(initial_array , writer):
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

def get_index_max_element_in_vector(scores_array):
    max_value = 0
    interaction_counter = 1
    element_counter = 1
    for score in scores_array:
        if (int(score) >= int(max_value)):
            max_value = score
            element_counter = interaction_counter
        interaction_counter += 1
    return element_counter

