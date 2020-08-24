# creation file with the students list
doc = input('Файл: ')
to_do = open(doc,'w')
while True:
    s = input()
    if s == '': break
    to_do.write(s+'\n')
to_do.close()