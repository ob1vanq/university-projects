# data = str(input("дата народження (03.09.2001): ")).split(".")

import numpy as np
c1, c2 = 'cornflowerblue', 'seagreen'

data = ['03', '09', '2001']
d1 = int(data[0][0])
d2 = int(data[0][1])
m1 = int(data[1][0])
m2 = int(data[1][1])
p1 = int(data[2][0])
p2 = int(data[2][1])
p3 = int(data[2][2])
p4 = int(data[2][3])

a = [1, (d1 + d2) / 140, (p2 - d2) / 130, -d1 / 250, -(m1 - d1) / 150]
b = [m1 / 10, (p3 - d2) / 20, -(m2 - m1) / 20, -p4 / 30, d2 / 20, -m2 / 20]

