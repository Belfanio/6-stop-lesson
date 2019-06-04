import random
class Human:
    def __init__(self, Name, Strength, Agility):
        self.Name = str(Name)
        self.Strength = int(Strength)
        self.Agility = int(Agility)
        self.soldier = list()
        self.hunter = list()
    def info(self):
        print('My name is {}'.format(self.Name))
        if self.Strength > 4: 
            print('I am very strong, Ill be a soldier')
        elif self.Agility > 5: 
            print('I am very clever, Ill be an hunter')
        else: 
            print('Ill be a farmer')   

print('Input name of Human')
name = str(input())
var = Human(Name = name, Strength = random.randint(1,5), Agility = random.randint(1,5))
print(var.info())
                

class Soldier(Human):
    pass
    def __init__(self, perk):
        Human.__init__(self, Name = var.Name, Agility=var.Agility, Strength = var.Strength)
        self.perk = str(perk)
    def soldier_info(self):
        print('hello, my name is {}, I am soldier, and I have a perk {}'.format(self.Name, self.perk))

print('Input perk from soldier')
perk = str(input())
var = Soldier(perk = perk)
print(var.soldier_info())


class Hunter(Human):
    pass
    def __init__(self, animal):
        Human.__init__(self, Name = var.Name, Agility=5, Strength = var.Strength)
        self.animal = str(animal)
    def hunter_info(self):
        print('hello, my name is {}, I am hunter, i hunt for {}'.format(self.Name, self.animal))

print('Input animal from hunter')
animal = str(input())
var = Hunter(animal = animal)
print(var.hunter_info())