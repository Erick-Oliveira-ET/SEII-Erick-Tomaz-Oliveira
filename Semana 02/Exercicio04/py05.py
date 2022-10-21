students = {"name": "Erick", "age": 21, "courses": ["SD", "SSA"]}

print(students)

print(students["name"])

print(students.get("phone", "Not Found"))

students["phone"] = "4478-5445"

print(students)

students["name"] = "Eric"

print(students)

students.update({"name":"Erick"})

print(students)

del students["age"]

print(students)

print(students.pop("phone"))

print(students)

print(len(students))

print(students.keys())

print(students.items())

for key, value in students.items():
  print( key, value)

