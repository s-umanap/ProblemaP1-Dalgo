#c.caro rama prueba
from os import strerror

try:
    ccnt = lcnt = 0
    stream = open("P1.in", "rt", encoding = "utf-8")
    line = stream.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
