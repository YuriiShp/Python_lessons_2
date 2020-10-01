import json
import os


class User:
    def __init__(self, name, last_name, age, **kwargs):
        self.pack = {'name': name, 'last_name': last_name, 'age': age, **kwargs}

    def info(self):
        for k, v in self.pack:
            print(f'{k}: {v}')

    def save(self, file_name):
        with open(file_name, 'a') as f:
            f.write(json.dumps(self.pack))


class Student(User):
    def __init__(self, name, last_name, age, university, course, **kwargs):
        super().__init__(name, last_name, age)
        self.pack = {'name': name, 'last_name': last_name, 'age': age,
                     'university': university, 'course': course, **kwargs}


class Employee(User):
    def __init__(self, name, last_name, age, company, position, **kwargs):
        super().__init__(name, last_name, age)
        self.pack = {'name': name, 'last_name': last_name, 'age': age,
                     'company': company, 'position': position, **kwargs}


# # Packing
# usr_1 = User(name='Erick', last_name='Cartman', age=10, loves='money')
# usr_2 = User(name='Kyle', last_name='Brofslovski', age=10, hates='Cartman')
# std_1 = Student(name='Ivan', last_name='Ivanov', age=20, university='DNU', course='physics')
# std_2 = Student(name='Mark', last_name='Shevchenko', age=21, university='Khai', course='math', year=5)
# emp_1 = Employee(name='Yurii', last_name='Shapoval', age=25, company='YSDO', position='engineer')
# emp_2 = Employee(name='Jeff', last_name='Besos', age=40, company='Amazon', position='CEO', race='alien')
#
# save_list = [usr_1, usr_2, std_1, std_2, emp_1, emp_2]
# for i in save_list:
#     i.save('users.txt')


# Unpacking
def sort_users(filename):
    with open(filename, 'r') as f:
        data = json.loads(f.read())

    usr_list = []
    stud_list = []
    emp_list = []
    other = []

    print(data)
    for el in data:
        if 'name' in el.keys() and 'last_name' in el.keys() and 'age' in el.keys():
            if 'university' in el.keys() and 'course' in el.keys():
                stud_list.append(Student(**el))
            elif 'company' in el.keys() and 'position' in el.keys():
                emp_list.append(Employee(**el))
            else:
                usr_list.append(User(**el))
        else:
            other.append(el)

    return usr_list, stud_list, emp_list, other


print(sort_users('users.txt'))
