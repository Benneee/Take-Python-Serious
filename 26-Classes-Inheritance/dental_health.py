import random

class DentalHealthItem():
  def __init__(self, price):
    self.price = price

class Toothbrush(DentalHealthItem):
  def use(self):
    return f'Brushing the teeth'

class Floss(DentalHealthItem):
  def use(self):
    return f'Flossing the teeth'

class Mouthwash(DentalHealthItem):
  def use(self):
    return f'Washing the teeth'


toothbrush = Toothbrush(150)
floss = Floss(600)
mouthwash = Mouthwash(1000)


dental_health_kit = [toothbrush, floss, mouthwash]
random.shuffle(dental_health_kit)

actions = [item.use() for item in dental_health_kit]
print(actions)

