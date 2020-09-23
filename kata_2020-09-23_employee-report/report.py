

def get_adult_employees(employees):
    adult_employees = []
    for employee in employees:
        age = employee['age']
        if age >= 18:
            adult_employees.append(employee)

    adult_employees = sorted(adult_employees, key = lambda i: i['name'], reverse = True)

    for employee in adult_employees:
        employee['name'] = employee['name'].upper()


    return adult_employees
