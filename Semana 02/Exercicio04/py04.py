courses = ["History", "Math", "Physics", "CompSci"]
courses_2 = ["Art", "Education"]

print(courses)

print(len(courses))

print(courses[0])

print(courses[-1])

print(courses[0:2])

print(courses[:2])

print(courses[2:])

courses.append("Art")

print(courses)

temp = courses
temp.insert(0, "Art")

print(temp)

temp = courses
temp.insert(0, courses_2)

print(temp)

temp = courses
temp.extend(courses_2)

print(temp)

temp = courses
temp.append(courses_2)

print(temp)

temp = courses
temp.remove("Math")

print(temp)

temp.pop()

print(temp)

nums = [1,5,2,7,4]

nums.sort()

print(nums)

nums.sort(reverse=True)

print(nums)

print(sorted(nums))

print(min(nums))

print(max(nums))

print(sum(nums))

print(courses.index("CompSci"))

for item in courses:
  print(item)

for index, course in enumerate(courses):
  print(course)

for index, course in enumerate(courses, start=1):
  print(course)

courses = ["History", "Math", "Physics", "CompSci"]


courses_str = ' - '.join(courses)

newList = courses_str.split(' - ')

print(courses_str)

print(newList)

tuple_1 = ("History", "Math", "Physics", "CompSci")

set_courses = {"History", "Math", "Physics", "CompSci", "Math"}
set_art_courses = {"History", "Math", "Art", "Design"}

print(set_courses)

print("Math" is set_courses)

print(set_courses.intersection(set_art_courses))
print(set_courses.difference(set_art_courses))
print(set_courses.union(set_art_courses))





