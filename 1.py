def create_table():
    table = [[0 for i in range(10)] for j in range(10)]
    return table
# print(create_table())
import random
def ships(table):
    i = 0
    locations = []
    
    locations_1 = list(map(int,input("Введіть координати для свого корабля через кому\n").split(",")))  
    if table[locations_1[0]][locations_1[1]] == 0 and locations_1[0] < 10 and locations_1[1] < 10:
        table[locations_1[0]][locations_1[1]] = 1
    else:
        print("Ці кординати вже зайняті, введіть інші")        
        ships(table)
    return table, locations_1
def ships2(table, num, loc1, loc2):
    position = input("Введіть v для вертикального рзміщення або  h для горизонтального розміщення ")
    if position == "v":
        for i in range(1, num):
            table[loc1+i][loc2] = 1
    else:
        for i in range(1, num):
            table[loc1][loc2 + i] = 1
    return table
    
def create_ships():
    table = create_table()
    for i in range(3):
        table, locs = ships(table)
        if i == 1:
            table = ships2(table, 3, locs[0], locs[1])
        if i==2:
            table = ships2(table, 4, locs[0], locs[1])
       
    return table
print(create_ships())
# def shoot(table):
#     while 
    
            
        
    
    
