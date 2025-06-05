class vechile:
    def _init_(self):
        pass
    def sound(self):
        return 'yeah all vechiles make sound!'
        # print('yeah all vechiles make sound!')
        
        
class car(vechile):
    def _init_(self):
        pass
    def sound(self):
        return 'yeah I car make sound like tu tutu'
    
class bike(vechile):
    def _init_(self):
        pass
    def sound(self):
        return 'yeah I bike make sound like rumrum'
    

car1 = car()
print(car1.sound())

bike1 = bike()
print(bike1.sound())