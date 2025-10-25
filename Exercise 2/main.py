
def get_cats_info(path):

    try:
        with open(path, 'r', encoding='utf-8') as cats_info:
              lines = [el.strip().split(',') for el in cats_info.readlines()]
              new_cats_info = []
              
              for id, name, age in lines:
                new_cats_info.append({"id": id, "name": name, "age": age})

        return new_cats_info
    
    except FileNotFoundError:
        return "File does not exist"
    except UnicodeDecodeError:
        return "File is damaged or it has incorrect coding"
    except PermissionError:
        return "You do not have permission on the file"
    
path = "/Users/Olena/Documents/University documents/goit-pycore-hw-04/goit-pycore-hw-04/Exercise 2/information_about_cats.txt"
cats_info = get_cats_info(path)
print(cats_info)
