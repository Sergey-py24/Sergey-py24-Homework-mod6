
class Animal:
    alive = True
    fed = False
    def __init__(self,name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не может есть {food}")

class Plant:
    edible = False
    def __init__(self,name):
        self.name = name


class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


an1 = Predator('Серый волк')
an2 = Mammal('Зайчик')
pl1 = Flower('Ромашка')
pl2 = Fruit('Яблоко')

print(an1.name)
print(an2.name)
print(an1.alive)
print(an2.fed)
an1.eat(pl1)
an2.eat(pl2)
print(an1.alive)
print(an2.fed)