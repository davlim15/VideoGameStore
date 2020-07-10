import openpyxl

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self._employee_id = employee_id
        self._salary = salary
        
    def __str__(self):
        return f"{self._employee_id}: {self.name} - {self.title}\t${self.salary}/yr"

    @property
    def employee_id(self):
        return self._employee_id


class Manager(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)
        self._title = "Store Manager"
        self._admin = True

    @property
    def employee_id(self):
        return super().employee_id

    @property
    def admin(self):
        return self._admin

class Associate(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)
        self._title = "Sales Associate"
        self._admin = False

    @property
    def employee_id(self):
        return super().employee_id

    @property
    def admin(self):
        return self._admin

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            self._title = new_title
        else:
            print("Invalid job title")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, int) and 30000 <= new_salary <= 60000:
            self._salary = new_salary
        else:
            print("Invalid salary")

class Team:
    def __init__(self):
        self._employees = {} #empty dictionary
        self.read_employees()

    @property
    def employees(self):
        return self._employees

    def read_employees(self):
        es = openpyxl.load_workbook("employees.xlsx").active

        #add employee from xl using ID as key and object as value
        for row in es.values:
            if row[0] == "manager":
                self._employees[row[2]] = Manager(row[1], row[2], row[3])
            elif row[0] == "associate":
                self._employees[row[2]] = Associate(row[1], row[2], row[3])

    def login(self, id_in): #pass in inputted ID to check if it exists in dictionary
        if id_in in self._employees.keys():
            return self._employees[id_in]
        return None
        

class Product:
    def __init__(self, title, type_, console, quantity, price):
        self.title = title
        self.type = type_
        self.console = console
        self._quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.console}: {self.title} - {self.price} - In stock: {self._quantity}"

    @property
    def quantity(self):
        return self._quantity
            

class Inventory:
    
    def __init__(self):
        self.cart = []
        self._products = {}
        self.read_products()
        
    @property
    def products(self):
        return self._products

    def read_products(self):
        ps = openpyxl.load_workbook("products.xlsx").active
        for row in ps.values:
            self._products[row[0]] = Product(row[1], row[2], row[3], int(row[4]), float(row[5]))

    def add_to_cart(self, i):
        if self.products[i]._quantity > 0:
            self.products[i]._quantity -= 1
            self.cart.append(self.products[i])
            print(f"{self.products[i].title} added to cart")
            #print(self.cart)
        else:
            print("There are no more of this item in stock")

    def empty_cart(self):
        self.cart = []

    def pay(self):
        total = 0
        for item in self.cart:
            total += item.price
        print(f"That will be ${total}. Thank you for shopping at VideoGameStore!\n")
        self.empty_cart()
        
        
