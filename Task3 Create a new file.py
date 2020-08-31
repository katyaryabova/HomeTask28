import re

with open('txt new') as grades_file:
    for line in grades_file:
        name, grades = re.split(":+", line)
        grades = [float(k) for k in grades.split()]
        avg = sum(grades) / len(grades)
        print("{} has an average grade of {:.2f}.".format(name, avg))
grades_file.close()
print()

for line in open('txt new', 'r', encoding='utf-8'):
    name, grades = re.split(":+", line)
    first_name, last_name = re.split(" ", name)
    short_name = last_name + ' ' + first_name[0] + '.'
    grades = [float(k) for k in grades.split()]
    avg = str(round(sum(grades) / len(grades),2))
    open('txt update8', 'a').write(f'{ "{0}{1}{2}".format(short_name, " ",  avg)}\n')

