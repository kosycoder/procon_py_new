n = int(input())
t = input()

state = "EAST"
x = 0
y = 0
for valt in t:
    if valt == "S":
        if state == "EAST":
            x += 1
        elif state == "SOUTH":
            y -= 1
        elif state == "WEST":
            x -= 1
        elif state == "NORTH":
            y += 1
    elif valt == "R":
        if state == "EAST":
            state = "SOUTH"
        elif state == "SOUTH":
            state = "WEST"
        elif state == "WEST":
            state = "NORTH"
        elif state == "NORTH":
            state = "EAST"

print(x, y)
