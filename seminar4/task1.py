""" Вычислить число Пи c заданной точностью d
Пример:
при d = 0.001, π = 3.141
при d = 0.1, π = 3.1
при d = 0.00001, π = 3.14154
d от 0.1 до 0.0000000001

!!! не округлять константу math
"""

from decimal import Decimal
from decimal import getcontext

def pi(rank):
    getcontext().prec=rank + 1
    result = 0
    for i in range (rank):
         result += (1/Decimal(16)**i * (Decimal(4)/(8*i+1) - Decimal(2)/(8*i+4) - Decimal(1)/(8*i+5) - Decimal(1)/(8*i+6)))
    return result
d = int(input('Введите количество разрядов после запятой: ')) 
print('π = ',pi(d))