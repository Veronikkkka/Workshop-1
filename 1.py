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
        table[locations_1[i]][locations_1[i+1]] = 1
    else:
        print("Ці кординати вже зайняті, введіть інші")        
        ships(table)
    return table
def create_ships():
    table = create_table()
    for i in range(3):
        if i == 1:
            table = ships(table)
        table = ships(table)
    return table
print(create_ships())
# def shoot(table):
#     while 
    
            
        
    
    
