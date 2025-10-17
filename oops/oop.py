class Car:
    def __init__(self,make,model,year,price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        
def display_info(self):
        return f"{self.year} {self.make} {self.model} -${self.price:,.2f}"

Car1 = Car("toyota","camry","2019","150000")

print(Car1.make)        