def hello_func():
  print("Hello Function")

print(hello_func)
print(hello_func())

hello_func()
hello_func()
hello_func()
hello_func()

def returned_hello_func():
  return "Hello Function"

print(returned_hello_func())
print(returned_hello_func().upper())

def greeting_hello_func(greeting):
  return f'{greeting} Function'

print(greeting_hello_func("hello"))


def name_hello_func(greeting, name="You"):
  return f'{greeting} {name} Function'

print(name_hello_func("hello"))


def student_info(*args, **kwargs):
  print(args)
  print(kwargs)

student_info("Math", "Art", name="John", age=22)

courses = ["History", "Math", "Physics", "CompSci"]
info = {"name": "Erick", "age": 21, "courses": ["SD", "SSA"]}

student_info(courses, info)

student_info(*courses, **info)


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))


