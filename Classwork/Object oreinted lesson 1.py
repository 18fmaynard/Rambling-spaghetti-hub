class fish():
    
    def __init__(self, species = "no species", age = 0, size = 0, colour = "no colour"):
        
        self.species = species
        self.age = age
        self.size = size
        self.colour = colour
        
    def speak(self):
        print("Hello I am a: ", self.species)
        print("I can live up to:", self.age)
        print("I can get up to: ", self.size)
        print("I am: ", self.colour)
        

blue_discus = fish("Blue Discus", 10, 15, "Blue")
red_discus = fish("Red Discus", 10, 15, "Red")


print(blue_discus.species)
blue_discus.speak()

print(red_discus.species)
red_discus.speak()