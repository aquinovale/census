import numpy as np
import random

def randomBellCurve():
    a = list()
    x = 55
    for i in range(1000):
        if(i == 20) or (i == 160) or (i == 500) or (i == 840) or (i == 980):
            x += 15
        a.append(random.randint(x,x + 15))
    return np.array(a)[random.randint(0,999)]

m70 = 0
m85 = 0
m100 = 0
m115 = 0
m130 = 0
m145 = 0
for i in range(1000000):
    value = randomBellCurve()

    if(value <= 70):
        m70 += 1
    elif(value <= 85):
        m85 += 1
    elif(value <= 100):
        m100 += 1
    elif(value <= 115):
        m115 += 1
    elif(value <= 130):
        m130 += 1
    else:
        m145 += 1
print("45 - 70: " + str(m70))
print("70 - 85: " + str(m85))
print("85 - 100: " + str(m100))
print("100 - 115: " + str(m115))
print("115 - 130: " + str(m130))
print("130 - 145: " + str(m145))
