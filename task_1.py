
def total_salary(path):
    total_salary = 0 
    try:
        with open(path, 'r') as input_file:
            data_from_file = input_file.readlines() 
            for person in data_from_file:
                name, salary = person.split(',')
                total_salary += float(salary)
    except FileNotFoundError:
        return print("File was not found")
    except ValueError:
        return print("Not enough data in file or wrong format of data") 
    except UnboundLocalError:
        return print("Cannot access local variable")
           
    avarage_salary = total_salary / len(data_from_file)
                
    salary_result = total_salary, avarage_salary
    print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {avarage_salary}")
    
    return salary_result

file = "C:/Users/sobol/Desktop/Projects/repositories/goit-algo-hw-04/goit-algo-hw-04/salaries.txt"

result = total_salary(file)
