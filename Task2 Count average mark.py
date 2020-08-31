# count average group mark and students  with the mark <5
# count average group mark and students  with the mark <5
from HomeTask28 import Color

f = open('txt new')
suma = 0
n = 0
for i in f:
    g = int(i[len(i)-2])
    suma += g
    n += 1
    if g < 5:
        print(i[:-1])
print(Color.Color.RED + 'Average mark: %.2f' % (suma / n) + Color.Color.END)
