class Car:
    def __init__(self,make,model,year,colour):
        self.make=make
        self.model=model
        self.year=year
        self.colour=colour
    def onyesha(self):
        print(f"I'd like a {self.colour} {self.make};the {self.model} model "
              f"manufactured in {self.year} ")
myobj=Car(colour="black",make="Mercedes",model="Maybach",year=2023)
myobj.onyesha()
myobj2=Car(colour="white" ,make="Ford",model="Ranger",year=2020)
myobj2.onyesha()