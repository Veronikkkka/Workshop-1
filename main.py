"""SHOOTING AND TRYING TO CREATE SHIP"""

def create_table():
    """
    This function creates table 10x10
    :return:
    """
    table = [["0" for i in range(10)] for j in range(10)]
    return table
table = create_table()


def create_ship(table):
    ship_info = []

    print("Ось ваша поточна дошка: ")
    for line in table:
        print(line)

    ship_facing = input("Поставте корабель: v - вертикально або h - горизонтально\n")
    ship_info.append(ship_facing)

    ship_length = input("Введіть довжину вашого корабля\n")
    ship_info.append(ship_length)

    ship_first_coordinate = list(map(int, input("Введіть через кому першу\
     координату, куди ставити корабель\n").split(",")))
    ship_info.append(ship_first_coordinate)

    return ship_info
print(create_ship(table))


def place_ships():
    pass


def shoot(table):
    shoot_coordinates = list(map(int, input("Введіть через кому координати, куди ви бажаєте здійснити постріл\n").split(",")))

    coordinate_x = shoot_coordinates[0] - 1
    coordinate_y = shoot_coordinates[1] - 1

    if table[coordinate_x][coordinate_y] == 1:
        table[coordinate_x][coordinate_y] = "X"
        print("Ви влучили! Зробіть постріл ще раз")
        return shoot(table)
    elif table[coordinate_x][coordinate_y] == "_":
        print("По цьому полі вже здійснювалася стрільба! Спробуйте ще раз")
        return shoot(table)
    else:
        table[coordinate_x][coordinate_y] = "_"
        print("На жаль, ви не влучили")
        return table

print(shoot(table))
