from rent import CarRent, BikeRent, Customer

bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

main_menu = True

while True:
    if main_menu:
        print("""
        **** Vehicle Rental Shop ****
        A. Bike Menu
        B. Car Menu
        C. Exit
        """)
        main_menu = False

        choice = input("Enter choice: ")

    if choice == "A" or choice == "a":
        print("""
        **** Bike Menu ****
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $84
        4. Return a bike
        5. Main Menu
        6. Exit
        """)

    choice = input("Enter choice: ")

    try:
        choice = int(choice)
    except ValueError:
        print("It is not integer")
        continue

    if choice == 1:
        bike.displayStock()
        choice = "A"
    
    elif choice == 2:
        customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
        customer.rentalBasis_b = 1
        main_menu = True
        print("----------------")
    
    elif choice == 3:
        customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
        customer.rentalBasis_b = 2
        main_menu = True
        print("----------------")
    
    elif choice == 4:
        bike.returnVehicle(customer.returnVehicle("bike"),"bike")
        customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
        main_menu = True

    elif choice == 5:
        main_menu = True

    elif choice == 6:
        break

    else:
        print("Invalid input. Please enter a number between 1-6")