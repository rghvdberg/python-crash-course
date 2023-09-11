from employee import Employee

programmer = Employee("John", "Doe", 50000)

print(programmer.first)
print(programmer.last)
print(programmer.salary)

programmer.give_raise()
print(programmer.salary)
programmer.give_raise(6969)
print(programmer.salary)
