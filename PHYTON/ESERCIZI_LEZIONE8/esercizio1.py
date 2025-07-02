import math

def safe_sqrt(number:float) -> int | float:
    try:
        return math.sqrt(number)
    except ValueError as error:
        return "Cannot compute square root of a negative number."

print(safe_sqrt(25))    
print(safe_sqrt(-9))