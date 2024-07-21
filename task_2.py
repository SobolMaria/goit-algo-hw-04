def get_cats_info(path):
    list_of_cats_info = []
    try:
        with open(path, 'r') as input_file:
            cats_info = input_file.readlines()
            
            for cat in cats_info:
                id, name, age = cat.strip().split(',')
                list_of_cats_info.append({"id": id, "name": name, "age": age})

    except FileNotFoundError:
        return "File was not found"
    except ValueError:
        return "Not enough data in file or wrong format of data" 
    except UnboundLocalError:
        return "Cannot access local variable"

    return list_of_cats_info


file = "C:/Users/sobol/Desktop/Projects/repositories/goit-algo-hw-04/goit-algo-hw-04/cats.txt"
print(get_cats_info(file))

    


