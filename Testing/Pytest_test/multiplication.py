# Multiplication File

import math

def addition(a: int, b: int) -> int:
    if any(not isinstance(data, int) for data in (a,b)):
        return 0
    return a + b

def sqrt(num):
    if not isinstance(num, int):
        raise ValueError(" Square root Error! Incorrect Input")
    return math.sqrt(num)

result = addition(52, 52)

print(result)