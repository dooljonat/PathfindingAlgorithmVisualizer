import math

# Floor a number to an interval
def floor_to_multiple(number, multiple):
    return multiple * math.floor(number / multiple)