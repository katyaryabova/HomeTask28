import re

with open('txt3') as grades_file:
    for line in grades_file:
        name, grades = re.split(":+", line)
        grades = [float(k) for k in grades.split()]
        avg = sum(grades) / len(grades)
        print("{} has an average grade of {:.2f}.".format(name, avg))

for line in open('txt3', 'r', encoding='utf-8'):
    name, grades = re.split(":+", line)
    grades = [float(k) for k in grades.split()]
    avg = sum(grades) / len(grades)
    if avg == int(avg):
        avg = int(avg)
    open('txt29', 'a').write(f'{name, avg}\n')
