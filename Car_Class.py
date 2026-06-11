class Car:
    def __init__(self, brand: str, horsepower: init)-> None:
        self.brand = brand
        self.horsepower = horsepower

    def drive(self):
        print(f"The {self.brand} with {self.horsepower} horsepower.")
    def get_info(self)-> None:
        return f"Brand: {self.brand}, Horsepower: {self.horsepower}"

volvo: Car=Car("Volvo", 200)