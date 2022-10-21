print("Hello World")

message = "Hello World"

print(message)

message = 'Erick\'s World'

print(message)

message = "Erick\'s World"

print(message)

message = """Erick's World is \
a crazy one"""

print(message)

print(len(message))

print(message[0:5])

print(message[6:])

print(message.count("World"))

print(message.find("World"))

print(message.replace("World", "Universe"))

greeting = "Hello"

name = "Erick"

message = greeting + ', ' + name

print(message)

message = '{}, {}. Welcome'.format(greeting, name)

print(message)

print(f'{greeting}, {name} from f format')

print(dir(name))

print(help(str.lower))
