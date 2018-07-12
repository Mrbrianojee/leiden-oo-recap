from employees.employee import Employee, Developer

# my_emp = Employee('Guido', "Van Rossom", 5)

# print(my_emp.get_details())


my_developer = Developer('Harry', "Wurth", 5, "JAVA")

# print(my_developer.get_details())


devs =  []
devs.append(my_developer)
print(devs[0].get_details())