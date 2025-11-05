
def total_salary (path):

    try:
        with open(path, 'r', encoding="utf-8") as salary_info:

            lines = [el.split(',') for el in salary_info.readlines()]

            new_salary_info = {}

            for employee_name, salary_range in lines:
                new_salary_info[employee_name] = float(salary_range.strip())
            
            total_salary_sum = 0
            for salary in new_salary_info.values():
                total_salary_sum += salary

            if len(new_salary_info) != 0:
                average_salary = total_salary_sum / len(new_salary_info)
            else: ZeroDivisionError

        return total_salary_sum, float(average_salary)
    except FileNotFoundError:
        return "File does not exist"
    except UnicodeDecodeError:
        return "File is damaged or it has incorrect coding"
        
path = "/Users/Olena/Documents/University documents/goit-pycore-hw-04/goit-pycore-hw-04/Exercise 1/month_salary.txt"
total, average = total_salary(path)
print(f"Total salary: {total}, Average salary: {average}")