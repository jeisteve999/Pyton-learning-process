class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday #{self.age}, {self.name}!")

# Instance of Person
paco = Person(name="Paco", age=20)
paco.have_birthday()


# Subclass Employee
class Employee(Person):

    def __init__(self, total_hours, name, age):
        super().__init__(name, age)
        self.total_hours = total_hours

    def work(self, hours_worked):
        self.total_hours += hours_worked
        print(f"You have worked {hours_worked} hours.")
        print(f"Total hours worked: {self.total_hours}")

# Instance of Employee
paco = Employee(name="Paco", age=20, total_hours=30)
paco.work(hours_worked=8)
paco.have_birthday()