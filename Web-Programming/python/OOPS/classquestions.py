class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 922/7 * self.radius ** 2
    
    def perimter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimter())



#q2
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

e1 = Employee("accountant", "Finance", "60000")
e1.showDetails()
eng1 = Engineer("Ayesha", 21)
eng1.showDetails()


#q3
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

order1 = Order("chips",20)
order2 = Order("tea", 15)

print(order1 > order2)
