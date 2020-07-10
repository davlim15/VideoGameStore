import objects

def menu(m):
    if m == "main":
        print(
            "VideoGameStore Cash Register System Main Menu\n" \
            "==========\n" \
            f"Employee: {cred.name}\n")
        print(
            "1. Checkout\n" \
            "2. Logout")
        if cred.admin:
            print("3. Manage Associates")

    elif m == "checkout":
        x = 1
        print("\nProducts in stock:")
        for key in products.products.keys():
            if products.products[key].quantity > 0:
                #shelf[key] = products.products[key]
                shelf.append(key)
                print(f"{x}. {products.products[key]}")
                x += 1
        if not bool(shelf):
            print("None")
        print("Press 0 to pay")

    elif m == "admin":
        print("\nAssociate Employee Management Portal\n==========")
        for e in employees.employees:
            if not employees.employees[e].admin:
                print(employees.employees[e])
                
    elif m == "admin2":
        print(
            f"\n{admin_select}\n" \
            "1. Change job title\n" \
            "2. Adjust salary\n" \
            "3. Exit")
        
    elif m == "admin3":
        print(
            "\n1. Sales Associate\n" \
            "2. Senior Sales Associate\n" \
            "3. Lead Sales Associate")
        
        
# Main Program
employees = objects.Team()
products = objects.Inventory()
shelf = []

while True:
    print("Welcome")

    # Login
    cred = None
    while cred == None:
        cred = int(input("Please enter your ID: "))
        cred = employees.login(cred)
        if cred == None:
            print("ID does not exist\n")
        else:
            print(f"Welcome, {cred.name}\n")

    # Main Menu
    menu_select = ""
    while True:
        menu("main")
        menu_select = input("\nSelect action: ")

        # Checkout
        if menu_select == "1":
            if bool(products.products):
                while True:
                    menu("checkout")
                    i = int(input("\nAdd item to cart: "))
                    if i == 0:
                        products.pay()
                        break
                    elif i > len(shelf) or not isinstance(i, int):
                        print("Invalid entry")
                    else:
                        products.add_to_cart(shelf[i-1])
                        shelf = []
            else:
                print("Store sold out")
                
        # Logout
        elif menu_select == "2":
            break
        
        # Manage Associates
        elif menu_select == "3" and cred.admin:
            admin_select = None
            while admin_select == None:
                menu("admin")
                admin_select = int(input("\nEnter an ID: "))
                admin_select = employees.login(admin_select)
                if admin_select != None and not admin_select.admin:
                    admin2_select = ""
                    while True:
                        menu("admin2")
                        admin2_select = input(f"\nSelect action for {admin_select.name}: ")
                        
                        # Change job title
                        if admin2_select == "1":
                            menu("admin3")
                            title_select = input(f"\nSelect new job title for {admin_select.name}: ")
                            if title_select == "1":
                                admin_select.title = "Sales Associate"
                            elif title_select == "2":
                                admin_select.title = "Senior Sales Associate"
                            elif title_select == "3":
                                admin_select.title = "Lead Sales Associate"
                            else:
                                print("Invalid selection")

                        # Adjust salary
                        if admin2_select == "2":
                            admin_select.salary = int(input(f"Enter new salary for {admin_select.title} {admin_select.name} ($30,000 - $60,000): "))

                        # Exit
                        if admin2_select == "3":
                            print()
                            break

                        # Default
                        else:
                            print("Invalid selection\n")
                        
                else:
                    print("ID does not exist or is not an associate ID")
                    admin_select = None

        # Default
        else:
            print("Invalid selection\n")

    #Logout
    print("Logout successful\n\n==========")
        
