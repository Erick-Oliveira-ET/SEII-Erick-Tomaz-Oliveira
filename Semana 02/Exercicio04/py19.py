from operator import attrgetter

li = [6,4,7,6,1,7,5,4,1]

s_li = sorted(li)

print( s_li)

li.sort()
print( li)

tup = (6,4,7,6,1,7,5,4,1)
print( sorted(tup))

di = {'name': 'Erick', 'Job': 'Fullstack JS', 'age': None, 'os': 'Windows'}
print(sorted(di)) 

li = [6,-4,7,6,-1,-7,5,-4,1]
s_li = sorted(li, key=abs)
print(s_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Erick', 21, 10923109)
e2 = Employee('Arthur', 22, 9314908)
e3 = Employee('Iuri', 43, 19231890)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name

s_employees = sorted(employees)

print(s_employees)

s_employees = sorted(employees, key=e_sort)

print(s_employees)

s_employees = sorted(employees, key=e_sort, reverse = True)

print(s_employees)

s_employees = sorted(employees, key=lambda: e: e.name)

print(s_employees)

s_employees = sorted(employees, key=attrgetter('age'))

print(s_employees)