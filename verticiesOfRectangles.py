#Given integer coordinates of three vertices of a rectangle whose sides are parallel to coordinate axes,
# find the coordinates of the fourth vertex of the rectangle. 

#Example input #1
#1
#5
#7
#5
#1
#10
#three vertices are (1, 5), (7, 5), (1, 10)

#Example output #1
#7
#10


def verticiesOfRectangles():
    x1 = int(input("Enter a number:"))
    y1 = int(input("Enter a number:"))

    x2 = int(input("Enter a number:"))
    y2 = int(input("Enter a number:"))

    x3 = int(input("Enter a number:"))
    y3 = int(input("Enter a number:"))

    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1
    
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1

    print(x4)
    print(y4)

verticiesOfRectangles()
