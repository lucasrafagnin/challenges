import sys

w, h = [int(i) for i in input().split()]
x0, y0 = [int(i) for i in input().split()]

xStart = 0
yStart = 0

def xPosition(direction):    
    global xStart, w
    if "R" in direction:
        xStart = x0
    elif "L" in direction:
        w = x0
    return (w + xStart) // 2


def yPosition(direction):    
    global yStart, h
    if "D" in direction:
        yStart = y0
    elif "U" in direction:
        h = y0
    return (h + yStart) // 2 

while True:
    direction = input()
    
    x0 = xPosition(direction)
    y0 = yPosition(direction)
    
    print("{x} {y}".format(x=x0, y=y0))
