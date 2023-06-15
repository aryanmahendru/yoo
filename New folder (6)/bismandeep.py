import json

class WashingMachine:
    def __init__(self):
        self.clothes = []
        self.timer = 0
        self.washing_type = None
        self.drying = False
        self.user_name = None
        self.history = []
        self.water_temperature = None

    def insert_clothes(self):
        clothes = input("Insert clothes use comma to separate the clothes: ").split(',')
        self.clothes.extend(clothes)
        print("Clothes inserted.")

    def remove_clothes(self):
        self.clothes.clear()
        print("All clothes removed.")

    def set_timer(self):
        duration = int(input("Set the timer please enter in minutes: "))
        self.timer = duration
        print("Timer set.")

    def select_washing_type(self):
        print("Available washing types:")
        print("1 Normal")
        print("2 Delicate")
        print("3 Heavy clothes")
        choice = input("Select washing type from 1-3: ")

        if choice == '1':
            self.washing_type = "Normal"
        elif choice == '2':
            self.washing_type = "Delicate"
        elif choice == '3':
            self.washing_type = "Heavyduty"
        else:
            print("Invalid choice washing type not selected.")

    def select_drying(self):
        drying = input("Select drying y for yes and n for no: ").lower() == 'y'
        self.drying = drying
        if drying:
            print("Drying option selected.")
        else:
            print("Drying option deselected.")

    def select_water_temperature(self):
        print("Available water temperature options:")
        print("1 Hot")
        print("2 Warm")
        print("3 Cold")
        choice = input("Select water temperature from 1-3: ")

        if choice == '1':
            self.water_temperature = "Hot"
        elif choice == '2':
            self.water_temperature = "Warm"
        elif choice == '3':
            self.water_temperature = "Cold"
        else:
            print("Invalid choice water temperature not selected.")
            return

        print("Water temperature set to:", self.water_temperature)

    def start(self):
        if not self.clothes:
            print("No clothes inserted please insert clothes.")
            return

        if not self.washing_type:
            print("No washing type selected please select a washing type.")
            return
        
        if self.timer == 0:
            print("Please set the timer to proceed.")
            return

        print("Starting the washing machine.")
        print("Washing type:", self.washing_type)
        print("Drying:", "Yes" if self.drying else "No")
        self.select_water_temperature()
        print("Timer set to:", self.timer, "minutes")
        print("Washing")

        while self.timer > 0:
            self.timer -= 1

        print("Washing complete")

        if self.drying:
            print("Drying")
            print("Drying complete")

        print("Please collect your clothes.")
        self.save_to_history()
        self.remove_clothes()

        

    def check_status(self):
        if self.timer > 0:
            print("Washing machine is running.")
        else:
            print("Washing machine is idle.")

    def cancel(self):
        self.timer = 0
        print("Washing process canceled.")

    def display_menu(self):
        print("Washing Machine Menu")
        print("1 Insert Clothes")
        print("2 Remove Clothes")
        print("3 Set Timer")
        print("4 Select Washing Type")
        print("5 Select Drying")
        print("6 Select Water Temperature")
        print("7 Start Washing Machine")
        print("8 Check Status")
        print("9 Cancel")
        print("0 Exit")

    def get_user_name(self):
        self.user_name = input("Enter your name: ")

    def load_history(self):
        try:
            with open('washing_history.json', 'r') as file:
                self.history = json.load(file)
        except FileNotFoundError:
            self.history = []

    def save_to_history(self):
        entry = {
            'User': self.user_name,
            'Clothes': self.clothes.copy(),
            'WashingType': self.washing_type,
            'Drying': self.drying,
            'WaterTemperature': self.water_temperature
        }
        self.history.append(entry)

        with open('washing_history.json', 'w') as file:
            json.dump(self.history, file, indent=4)

    def simulate(self):
        self.get_user_name()
        self.load_history()

        amount = 3

        while True:
            proceed = input(f"Please insert ${amount} to proceed y for yes and n for no: ")

            if proceed.lower() != 'y':
                print("Payment not made exiting.")
                return

            print("Payment made washing machine is ready.")

            while True:
                self.display_menu()
                choice = input("Enter your choice: ")

                if choice == '1':
                    self.insert_clothes()

                elif choice == '2':
                    self.remove_clothes()

                elif choice == '3':
                    self.set_timer()

                elif choice == '4':
                    self.select_washing_type()

                elif choice == '5':
                    self.select_drying()

                elif choice == '6':
                    self.select_water_temperature()

                elif choice == '7':
                    self.start()

                elif choice == '8':
                    self.check_status()

                elif choice == '9':
                    self.cancel()

                elif choice == '0':
                    print("Exiting the program.")
                    return

                else:
                    print("Invalid choice. Please try again.")


# Main program
if __name__ == '__main__':
    washing_machine = WashingMachine()
    washing_machine.simulate()
