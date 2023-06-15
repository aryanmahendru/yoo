import json

def loadcarstock():
    try:
        with open("carstock.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def savecarstock(carstock):
    with open("carstock.json", "w") as file:
        json.dump(carstock, file)


def loadloandetails():
    try:
        with open("loandetails.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def saveloandetails(loandetails):
    with open("loandetails.json", "w") as file:
        json.dump(loandetails, file)


def addcar(carstock):
    while True:
        car_id = input("Enter car ID: ")
        if not car_id.isdigit():
            print("Invalid car ID. Please enter a number.")
            continue

        
        if car_id in carstock:
            print("Car ID already exists.")
        else:
            break
    name = input("Enter car name: ")
    model = input("Enter car model: ")
    make = input("Enter car make: ")
    price = float(input("Enter car price: $"))
    stock = int(input("Enter car stock: "))
    car_info = {'name': name, 'model': model, 'make': make, 'price': price}
    carstock[car_id] = {'info': car_info, 'stock': stock}
    print("Car added successfully.")


def add_update_remove_car(carstock):
    print("\nManage Car Stock:")
    print("1. Add a New Car")
    print("2. Update Car Stock")
    print("3. Remove a Car")
    choice = input("Enter your choice: ")

    if choice == "1":
        addcar(carstock)

    elif choice == "2":
        car_id = input("Enter car ID: ")
        if car_id not in carstock:
            print("Car ID does not exist.")
            return
        stock = int(input("Enter updated car stock: "))
        carstock[car_id]['stock'] = stock
        print("Car stock updated successfully.")

    elif choice == "3":
        car_id = input("Enter car ID: ")
        if car_id not in carstock:
            print("Car ID does not exist.")
            return
        del carstock[car_id]
        print("Car removed successfully.")

    else:
        print("Invalid choice.")


def car_loan_system():
    # Loading car stock and loan details
    carstock = loadcarstock()
    loandetails = loadloandetails()

    while True:
        # Ask user for viewing prevoius loan and other loan  options
        print("\nChoose an action:")
        print("1. View Previous Loans")
        print("2. Manage Car Stock")
        print("3. Start a New Loan")
        print("4. Exit")
        action = input("Enter your choice: ")

        if action == "1":
            # Display previous loans
            print("\nPrevious Loans:")
            for loan in loandetails:
                print(loan)

        elif action == "2":
            # managing car stocks
            add_update_remove_car(carstock)
            savecarstock(carstock)

        elif action == "3":
            # displaying car options
            print("\nCar Options:")
            for car_id, car_info in carstock.items():
                stock = car_info['stock']
                print(f"{car_id}. {car_info['info']['name']} - {car_info['info']['make']} {car_info['info']['model']} - ${car_info['info']['price']} - Stock: {stock}")

            # ask user for user choice
            car_choice = input("Enter the car ID you want to purchase: ")
            selected_car = carstock.get(car_choice)
            if not selected_car:
                print("Invalid car choice.")
                continue

            # checking car stock
            if selected_car['stock'] == 0:
                print("Sorry, the selected car is out of stock.")
                continue

            # asking user for perosnal details
            name = input("Enter your name: ")
            salary = float(input("Enter your monthly salary: $"))
            down_payment = float(input("Enter the down payment amount: $"))
            loan_duration = int(input("Enter the loan duration (in years): "))

            # calculating loan ammount
            car_price = selected_car['info']['price']
            loan_amount = car_price - down_payment

            # calculating monthly payment
            months = loan_duration * 12
            interest_rate = 0.05  # 5% interest rate per year
            monthly_interest_rate = interest_rate / 12
            monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)

            # Check if monthly payment is within 20% of the salary
            if monthly_payment <= 0.2 * salary:
                print("\nLoan Approved!")
                bank_details = input("Enter your bank details: ")
                print("Congratulations! Your loan has been approved.")
                print(f"Monthly Payment: ${monthly_payment:.2f}")
                print(f"Car Name: {selected_car['info']['name']}")
                print(f"Model: {selected_car['info']['model']}")
                print(f"Make: {selected_car['info']['make']}")
                print(f"Price: ${car_price}")
                print(f"Loan Duration: {loan_duration} years")
                print(f"Loan Amount: ${loan_amount:.2f}")
                print(f"Bank Details: {bank_details}")

                # Reduce car stock
                selected_car['stock'] -= 1
                savecarstock(carstock)

                # Save loan details
                loan_info = {
                    'Name': name,
                    'Car Name': selected_car['info']['name'],
                    'Model': selected_car['info']['model'],
                    'Make': selected_car['info']['make'],
                    'Price': car_price,
                    'Loan Duration': loan_duration,
                    'Loan Amount': loan_amount,
                    'Monthly Payment': monthly_payment,
                    'Bank Details': bank_details
                }
                loandetails.append(loan_info)
                saveloandetails(loandetails)
            else:
                print("\nLoan Disapproved. Monthly payment exceeds 20% of your salary.")

        elif action == "4":
            break

        else:
            print("Invalid choice.")


# Run the car loan system
car_loan_system()