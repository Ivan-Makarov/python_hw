class Animal:
    weight = 0.0  # kg
    max_weight = 0.0  # kg


class FarmAnimal(Animal):
    is_tame = True
    feed_efficiency = 1  # kgs of food tranfsormed into 1 kg of weight
    max_food_per_day = 1  # kg

    def __init__(self, weight_at_birth=Animal.weight):
        self.weight = weight_at_birth

    def feed(self, food_amount):
        if food_amount > self.max_food_per_day:
            food_amount = self.max_food_per_day
        if self.weight < self.max_weight:
            self.weight += food_amount / self.feed_efficiency
            if self.weight > self.max_weight:
                self.weight = self.max_weight


class Bird(Animal):
    legs = 2
    has_wings = True


class Mammal(Animal):
    legs = 4


class Cow(Mammal, FarmAnimal):
    feed_efficiency = 6
    weight = 30
    max_weight = 400
    max_food_per_day = 100
    gives = [
        'milk',
        'meat',
        'hide'
    ]
    says = 'Moo'


class Goat(Mammal, FarmAnimal):
    weight = 3.5
    max_weight = 50
    max_food_per_day = 30
    feed_efficiency = 5
    gives = [
        'milk',
        'meat',
        'wool',
        'hide'
    ]
    says = 'Maaah'


class Sheep(Mammal, FarmAnimal):
    weight: 4
    feed_efficiency = 4
    max_weight = 60
    max_food_per_day = 35
    gives = [
        'milk',
        'meat',
        'wool'
    ]
    says = 'Baaah'


class Pig(Mammal, FarmAnimal):
    weight: 2.5
    max_weight = 200
    max_food_per_day = 80
    gives = [
        'meat'
    ]
    says = 'Oink-oink'


class Duck(Bird, FarmAnimal):
    weight: 0.05
    feed_efficiency = 2.5
    max_weight = 4
    max_food_per_day = 3
    gives = [
        'eggs',
        'meat'
    ]
    says = 'Quack-quack'


class Chicken(Bird, FarmAnimal):
    weight: 0.04
    feed_efficiency = 2
    max_weight = 3
    max_food_per_day = 2.5
    gives = [
        'eggs',
        'meat'
    ]
    says = 'Cluck-cluck'


class Goose(Bird, FarmAnimal):
    weight: 0.1
    feed_efficiency = 3.5
    max_weight = 7
    max_food_per_day = 5
    gives = [
        'eggs',
        'meat'
    ]
    says = 'Honk'


cow_1 = Cow(35)
duck_1 = Duck(0.07)


def show_weight_growth(animal, days, food_per_day):

    for day in range(1, days + 1):
        if animal.weight == animal.max_weight:
            print("День {}, достигнут максимальный вес {} кг".format(day, animal.max_weight))
            break
        print("День {}, вес: {}".format(day, animal.weight))
        animal.feed(food_per_day)


show_weight_growth(cow_1, 100, 30)
show_weight_growth(duck_1, 100, 3)
