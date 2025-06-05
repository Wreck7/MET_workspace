class AC: 
    def _init_(self, brand): 
        self.brand = brand 
        
    def turn_on(self): 
        print(f"{self.brand} Ac turned on") 
    def turn_off(self): 
        print("Ac turned off") 
    def change_temp(self): 
        pass 

class Light: 
    def _init_(self, watts):
        self.watts = watts
    def turn_on(self):
        print(f'{self.watts}w light is turned on!')
    
class Room: 
    def _init_(self, ac, light): 
        self.temp = 24 
        self.ac = ac
        self.light = light
    
ac = AC("samsung") 
light = Light(100)

room = Room(ac, light)
room.ac.turn_on()
room.light.turn_on()