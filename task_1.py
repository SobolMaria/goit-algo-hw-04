
def total_salary(path):
    try:
        with open(path, 'r') as input_file:
            data_from_file = input_file.readlines()
    except FileNotFoundError:
        print("File was not found")
    except ValueError:
        print("Not enough data in file or wrong format of data") 
    
    total_salary = 0

    for person in data_from_file:
        name, salary = person.split(',')
        total_salary += float(salary) 
                
    avarage_salary = total_salary / len(data_from_file)
                
    salary_result = total_salary, avarage_salary
    print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {avarage_salary}")

    return salary_result

file = 'C:/Users/sobol/Desktop/Projects/repositories/goit-algo-hw-04/salaries.txt'

result = total_salary(file)
