def printSomething(word):
    print(word)

def addTwoNumbers(x, y):
    print(x)
    print(y)
    print(x + y)

def printMultipleTimes (word, numberOfTimesToPrint) :
    for i in range (0, numberOfTimesToPrint) :
        print(str(i) + " " + word)

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def changeName(self, newName):
        self.name = newName
    

dogOne = Dog("chilla", "borderCollie", 15)
dogTwo = Dog("charlie", "kelpie", 7)

print(dogOne.name)

dogOne.changeName("bob")

print(dogOne.name)

# challenge: make a new class: Car
# which is constructed with properties: make, model, year
