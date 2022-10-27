class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def show(self):
    print(f"I am {self.name} and I am {self.age} years old")

  def speak(self):
    print("Don't know what to say")

class Dog(Pet):
  def speak(self):
    print("Bark")

class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color

  def speak(self):
    print("Meow")

  def show(self):
    print(f"I am {self.name} and I am {self.age} years old and I'm {self.color}")


class Fish(Pet):
  pass

p = Pet('Tim', 19)
p.show()
c.speak()
c = Cat("Bill", 34, "Blue")
c.show()
c.speak()
d = Dog("Jill", 25)
d.show()
d.speak()

f = Fish("Jill", 25)
f.speak()