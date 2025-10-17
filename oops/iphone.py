class Iphone:
    def __init__(self,model,year,color):
        self.model = model
        self.year = year
        self.color = color
        
    def display_info(self):
        return f"your {self.model}  release year is o{self.year} youer phone color is {self.color}"

Iphone1 = Iphone("iphone 17 pro","2025","orange")
print(Iphone1.display_info())

