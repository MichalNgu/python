import random

w = 9
h = 3
mines = 8

# generate field
field = []
for x in range(w):
    row = []
    for y in range(h):
        row.append(0)
    field.append(row)

# put mines in random positions
for i in range(mines):
    while True:
        rx = random.randint(0, w - 1)
        ry = random.randint(0, h - 1)
        if field[rx][ry] != "M":
            field[rx][ry] = "M"
            break

# print field
for y in range(h):
    for x in range(w):
        print(field[x][y], end="")
    print()