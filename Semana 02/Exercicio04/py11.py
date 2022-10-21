f = open("text.txt", "r")

print(f.name)
print(f.mode)

f.close()

with open("text.txt", "r") as f:
  f_contents = f.read()
  print(f_contents)

  f.seek(0)

  f_contents = f.readlines()
  print(f_contents)

  f_contents = f.readline()
  print(f_contents)

  f_contents = f.readline()
  print(f_contents)

  f.seek(0)


  for line in f:
    print(line, end='')

  f.seek(0)

  f_contents = f.read(15)
  print(f_contents)

  print(f.tell())

  f_contents = f.read(15)
  print(f_contents)

with open("test2.txt", 'w') as f:
  f.write("Test")
  f.write("Test2")

with open("text.txt", "r") as rf:
  with open("test_copy.txt", 'w') as wf:
    for line in rf:
      wf.write(line)

# with open("text.jpg", "rb") as rf:
#   with open("test_copy.txt", 'w') as wf:
#     for line in rf:
#       wf.write(line)
