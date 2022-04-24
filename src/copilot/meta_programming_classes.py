import abc
import random

CLASS_NAMES = ["Apple", "Banana", "Cherry",  "Grape", "Honeydew", "Jackfruit",
               "Kiwi", "Mango", "Orange", "Papaya", "Raspberry", "Strawberry"]


class Fruit(abc.ABC):

    def __init__(self, id, ripe: bool = True, expired: bool = True):
        self.ripe = ripe
        self.expired = expired
        self.id = id
        self.days_checked = 0

    def check_for_expiring(self):
        # easy logic just for demonstration. No real logic here.
        if random.random() < 0.1 * self.days_checked:
            self.expired = True
        else:
            self.expired = False
        self.days_checked += 1
        return self.expired


for i in CLASS_NAMES:
    exec("""class {}(Fruit): pass""".format(CLASS_NAMES[0]))

apple = Apple(1)
print("Apple expired: {}".format(apple.check_for_expiring()))