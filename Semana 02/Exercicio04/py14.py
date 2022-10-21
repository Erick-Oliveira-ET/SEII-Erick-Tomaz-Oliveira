import os

os.chdir('')

for f in os.listdir():
  file_name, file_ext = os.path.splitext(f)

  f_title, f_course, f_num = file_name.split('-')

  f_title =f_title.strip()
  f_course =f_course.strip()
  f_num =f_num.strip()[1:].zfill(2)

  new_name=f'{f_num}-{f_course}-{f_title}{file_ext}'

  os.rename(f, new_name)