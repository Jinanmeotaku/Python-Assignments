#Given 3 points (each with an x & y-value), determine the perimeter of the triangle it creates. 
#Note that the triangles aren't necessarily right triangles.

#Example input
#0, 0, 3, 0, 0, 4

#Example output
#12.0

import math
def trianglePirameter(x1, y1, x2, y2, x3, y3):
    
    AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    CA = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    
    return AB + BC + CA

print(trianglePirameter(0, 0, 3, 0, 0, 4)) #12.0
