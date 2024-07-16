def get_cats_info(path):
    try:
        with open(path, 'r') as input_file:
            cats_info = input_file.readlines()
    except FileNotFoundError:
        print("File was not found")
    except ValueError:
        print("Not enough data in file or wrong format of data") 
    list_of_cats_info = []
    dict_of_cats_info = {}
       
    for cat in cats_info:
        id, name, age = cat.split(',')
        dict_of_cats_info['id'] = id
        dict_of_cats_info['name'] = name
        dict_of_cats_info['age'] = age
        list_of_cats_info.append(dict_of_cats_info)

    return list_of_cats_info


file = 'C:/Users/sobol/Desktop/Projects/repositories/goit-algo-hw-04/cats.txt'
print(get_cats_info(file))

    


