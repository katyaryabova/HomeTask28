# count average group mark and students  with the mark <5
f = open('txt3')
suma = 0
n = 0
for i in f:
    g = int(i[len(i)-2])
    suma += g
    n += 1
    if g < 5:
        print(i[:-1])
print('Average mark: %.2f' % (suma / n))