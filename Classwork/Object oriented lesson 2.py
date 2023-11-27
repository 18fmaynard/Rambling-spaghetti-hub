class fruit():
    
    def __init__(self, colour = "unknown", size = "unknown", taste = "unknown"):
        
        self.colour = colour
        self.size = size
        self.taste = taste
        
class tropical_fruit(fruit):

    def __init__(self, colour, size):
        super().__init__(colour, size, "sweet")
        
    def show_properties(self):
        print(self.colour, self.size, self.taste)
        
mango = tropical_fruit("green/red", "medium")

mango.show_properties()