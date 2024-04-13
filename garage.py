class Vehicle():
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        # self.transmission = transmission
        
    def drive(self):
        print(f'skirrrrt')
    def turn(self):
        print(f'Your vehicle turned left')
    def stop(self):
        print(f'Your vehicle just stopped!')
        
class S2K(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
    def drive(self):
        print("The s2k drives past.")
        
class Stormy(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
    def turn(self):
        print('Your {self.model} turned {direction}')
        
class Shirley(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
    def drive(self):
        print("The {self.color} {self.model} drives past.")
        
class Spirit(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
    def stop(self):
        print("Your {self.color} {self.make} stopped.")
        
class Smokey(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
    def drive(self):
        print("The {self.color} {self.model} drives past.")
        
s2k = S2K("Honda", "S2000", "2004", "green")
smokey = Smokey("Volvo", "850", "1999", "black")
stormy = Stormy("Subaru", "Forester", "2015", "silver")
spirit = Spirit("Subaru", "Forester", "2020", "black")
shirley = Shirley("Honda", "CRV", "1997", "green")

s2k.drive()
smokey.drive()
spirit.drive()

s2k.turn()
smokey.turn()
shirley.turn()

smokey.stop()