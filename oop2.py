class Fruits:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(f"I bought {self.name} at {self.price}")
obj1=Fruits(name="Mangoes",price="Ksh.50")
obj1.display()
obj2=Fruits(name="Apples",price="Ksh.30")
obj2.display()
obj3=Fruits(name="Bananas",price="Ksh.10")
obj3.display()
obj4=Fruits(name="Oranges",price="Ksh.20")
obj4.display()
obj5=Fruits(name="Watermelons",price="Ksh.100")
obj5.display()
