class Dog:
  def __init__(self, name):
    self.name = name
    print(name)

  def add_node(self, x):
    return x +1

  def bark(self):
    print("bark")

d = Dog("Tim")
d = Dog("Bill")