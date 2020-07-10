# VideoGameStore
Capstone project for Python Object Oriented Programming Udemy course

Employee
This is a parent class that holds the common attributes shared among Managers and Associates (name, employee id, and salary)
The class contains a special string function that prints the employee information in a readable format, and a getter for the ID

Manager
Inherits from Employee. Additional attributes are title="Store Manager" and admin=True. These are both private variables and cannot be changed from within the program - only accessed through getters. The admin bool grants the additional "Manage Associates" option on the main menu.

Associate
Inherits from Employee. Additional attributes are title="Sales Associate" and admin=False. This class additionally include getters and setters for job title and salary, which are controlled from within the class or a menu in the main program.

Team
This is an independant class that hold a dictionary of all the employees and functional methods to handle reading from employees.xlsx and login.

Product
Product contains the attributes for each unique product. It contains a special string function to display the product information and a quantity getter, a private variable controlled by another method in...

Inventory
This class handles all the data for performing checkout of products. A dictionary stores all of the product information, and the cart variable tracks which items are moved from inventory to cart. Functional methods are included for reading the product information from the excel file, adding the total price of cart contents, and emptying the cart after the transaction is complete.

To do: Write changes made in system back to the excel files upon logout
