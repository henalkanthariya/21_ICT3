
class AccessDeniedError(Exception):
    pass


class Car:
    def __init__(self, brand, model, price, fuel_type, transmission, color):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.color = color

    def show_details(self):
        return (f"Brand: {self.brand}\n"
                f"Model: {self.model}\n"
                f"Price: ₹{self.price}\n"
                f"Fuel Type: {self.fuel_type}\n"
                f"Transmission: {self.transmission}\n"
                f"Color: {self.color}\n")


class Showroom:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, model_name):
        for car in self.cars:
            if car.model.lower() == model_name.lower():
                self.cars.remove(car)
                return car
        return None

    def list_cars(self):
        if not self.cars:
            print("No cars available in showroom.")
        else:
            for i, car in enumerate(self.cars, 1):
                print(f"{i}. {car.brand} {car.model} - ₹{car.price}")


def main():
    showroom = Showroom()

  
    showroom.add_car(Car("Toyota", "Camry", 2500000, "Petrol", "Automatic", "White"))
    showroom.add_car(Car("Hyundai", "i20", 800000, "Petrol", "Manual", "Red"))
    showroom.add_car(Car("Tata", "Nexon", 1200000, "Petrol", "Manual", "Blue"))

    while True:
        print("\n--- Car Showroom Management ---")
        print("1. View Available Cars")
        print("2. Display Car Details")
        print("3. Sell a Car")
        print("4. Buy a Car")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            showroom.list_cars()

        elif choice == "2":
            try:
                salary = int(input("Enter your salary: "))
                if salary < 100000:
                    raise AccessDeniedError("Salary less than ₹1,00,000. Access denied!")

                model = input("Enter model name to view details: ")
                found = False
                for car in showroom.cars:
                    if car.model.lower() == model.lower():
                        print(car.show_details())
                        found = True
                        break
                if not found:
                    print("Car not found!")

            except AccessDeniedError as e:
                print(e)

        elif choice == "3":
            model = input("Enter model name to sell/remove: ")
            car = showroom.remove_car(model)
            if car:
                print(f"{car.brand} {car.model} removed from showroom.")
            else:
                print("Car not found!")

        elif choice == "4":
            brand = input("Brand: ")
            model = input("Model: ")
            price = int(input("Price: "))
            fuel = input("Fuel type: ")
            transmission = input("Transmission: ")
            color = input("Color: ")
            showroom.add_car(Car(brand, model, price, fuel, transmission, color))
            print("Car added successfully!")

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
