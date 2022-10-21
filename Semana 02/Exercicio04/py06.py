if True:
  print("Condição é verdadeira")

if False:
  print("Condição é falsa")

language = "Python"

if language == "Python":
  print("Linguagem é python")
else:
  print("No match")

language = "Python"

if language == "Java":
  print("Linguagem é Java")
else:
  print("No match")

if language == "Python":
  print("Linguagem é Python")
elif language == "Java":
  print("Linguagem é Java")
elif language == "Javascript":
  print("Linguagem é Javascript")
else:
  print("No match")

user = "Admin"
logged_in = True

if user == "Admin" and logged_in:
  print("Admin Page")
else:
  print("Bad credentials")

user = "Client"
logged_in = True

if user == "Admin" and logged_in:
  print("Admin Page")
else:
  print("Bad credentials")

user = "Client"
logged_in = True

if user == "Admin" or logged_in:
  print("Admin Page")
else:
  print("Bad credentials")

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)

print(id(a))
print(id(b))
print(a == b)

a = b

print(id(a))
print(id(b))
print(a == b)

if None:
  print("Evaluated to True")
else:
  print("Evaluated to False")

if 0:
  print("Evaluated to True")
else:
  print("Evaluated to False")

if []:
  print("Evaluated to True")
else:
  print("Evaluated to False")
