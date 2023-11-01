import math

def score(x, y):
    distance_to_center = math.sqrt(x**2 + y**2)
    
    if distance_to_center <= 1:
        return 10
    elif distance_to_center <= 5:
        return 5
    elif distance_to_center <= 10:
        return 1
    else:
        return 0
