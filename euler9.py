# a^2 * b^2 = c^2 = (1000-a-b)^2
# = 1000^2 + a^2 + b^2 + 2ab - 2000a - 2000b
# 2000a + 2000b = 1000^2 + 2ab
# b = (1000^2 - 2000a)/(2000-2a)

import math

for a in range(2,1000) :
    b1, b2 = (1000*1000 - 2000*a) , (2000-2*a)
    if b1 % b2 == 0 and b1 > b2 > 0 :
        b = b1 / b2
        c = math.sqrt(a*a+b*b)
        print a,b,c, a*b*c
