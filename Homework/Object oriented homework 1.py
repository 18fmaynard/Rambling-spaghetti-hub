class animals():
    def __init__(self, animal_species = "unknown", age = 0, threat_level = "peaceful", hunger_level = 0):
        self.animal_species = animal_species
        self.age = age
        self.threat_level = threat_level
        self.hunger_level = hunger_level
    def set_species(self):
        self.animal_species = input("Enter the species name: ")
        return(self.animal_species)
    def set_age(self):
        self.age = int(input("How old is the animal? "))
        return(self.age)
    def set_hunger_level(self):
        self.age = int(input("How hungry is the animal (1-10)? "))
        return(self.hunger_level)
    def change_threat_level(self):
        if self.age <= 3:
            self.threat_level = "Peaceful"
        elif 4 <= self.age <=7:
            self.threat_level = "Narky"
        else:
            self.threat_level = "Aggressive"
        return(self.threat_level)
    def giveinfo(self):
        print(self.animal_species)
        print("Age: ", self.age)
        print("Hunger level: ", self.hunger_level)
        print("Threat level: ", self.threat_level)
def add_animal():          
    animal_to_add = input("What animal would you like to add? ")
    animal_to_add = animals()
    animal_to_add.set_species()
    animal_to_add.set_age()
    animal_to_add.set_hunger_level()
    animal_to_add.change_threat_level()
    animal_to_add.giveinfo()
    add_animal()
add_animal()