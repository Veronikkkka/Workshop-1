import random

def create_table():
    table = [[0 for i in range(10)] for j in range(10)]
    return table

def create_ships():
    pass

def shoot():
    table = create_table()
    shoot_coordinates = list(map(int, input("Введіть через кому координати, куди ви бажаєте здійснити постріл\n").split(",")))

    coordinate_x = shoot_coordinates[0] - 1
    coordinate_y = shoot_coordinates[1] - 1

    if table[coordinate_x][coordinate_y] == 1:
        table[coordinate_x][coordinate_y] = "X"
    else:
        table[coordinate_x][coordinate_y] = "_"

    return table

print(shoot())
