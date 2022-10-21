import os
from datetime import datetime

print(dir(os))

print(os.getcwd())

os.chdir("C:\Users\erick\OneDrive - Universidade Federal de Uberlândia\Engenharia Mecatrônica\8° Período\Sistemas Digitais para Mecatrônica\SEII\SEII-Erick-Tomaz-Oliveira\Semana 02")

print(os.getcwd())

print(os.listdir())

os.mkdir("teste")
os.makedirs("teste2/profound")

print(os.listdir())

os.rmdir("teste")
os.removedirs("teste2/profound")

print(os.listdir())

os.rename("test.txt", "demo.txt")

print(os.stat("demo.txt"))

mod_time = os.stat("demo.txt").st_mtime
print(mod_time)
print(datetime.fromtimestamp(mod_time))

os.chdir("C:\Users\erick\OneDrive - Universidade Federal de Uberlândia\Engenharia Mecatrônica\8° Período\Sistemas Digitais para Mecatrônica\SEII\SEII-Erick-Tomaz-Oliveira\Semana 02")
for dirpath, dirnames, filenames in os.walk("C:\Users\erick\OneDrive - Universidade Federal de Uberlândia\Engenharia Mecatrônica\8° Período\Sistemas Digitais para Mecatrônica\SEII\SEII-Erick-Tomaz-Oliveira\Semana 02"):
  print("Current Path: ", dirpath)
  print("Directiories: ", dirnames)
  print("Files: ", filenames)

print(os.environ.get("HOME"))

file_path = os.path.join(os.environ.get("HOME"), "test.txt")

print(file_path)


