class Human:
    def __init__(self, age, name):
        self.age = int(age)
        self.name = str(name)
    def say_hello(self):
        print('hello, my name is {}'.format(self.name))

var = Human(age = 28, name= 'Sergey')
print(var.say_hello())

class Builder(Human):
    pass
    def __init__(self, profession):
        Human.__init__(self, name = var.name, age=var.age)
        self.profession = str(profession)
    def say_hello(self):
        print('hello, my name is {}, I am is {}'.format(self.name, self.profession))

var = Builder( profession='Ingener')
print(var.say_hello())

class Writer(Human):
    pass
    def __init__(self, books):
        self.books = books
    def my_books(self):
        print('I write {} books'.format(len(self.books)))

var = Writer(books = ['Age of Impire', 'Tapmle of the Dark', 'Ishimura'])
print(var.my_books())