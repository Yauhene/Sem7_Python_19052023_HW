# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# Ввод: 
# print_operation_table(lambda x, y: x * y)
 
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36
r_num = 6
c_num = 6

def print_operation_table(operation, num_rows=6, num_columns=6):
    list_rows = [x for x in range(1,r_num+1)]
    list_columns =[x for x in range(1, c_num+1)]
    #print(list_rows)
    for x in list_rows:
        print("{:4d}".format(x), end='')
    print()    
    print("{:4d}".format(list_columns[1]), end='')
    for i in range(1,r_num):
        #print(f'i = {i}')
        #print(list_columns[2], end='')
        for j in range(1,c_num):
            #pass
            #print(f'i = {i}, j = {j}  ', end='')

            #print([j], end ='')
            #print(f"{calk_1(i, j):.3}")
            print("{:4d}".format(calk_1(list_columns[j],list_rows[i])), end='')
            #print(calk_1(list_columns[i],list_rows[j]), end='')
            #x = calk_1(i, j)
            # print(f'x = {x}')
            #print(f'   i = {i}, j = {j}  ')

        print()


calk_1 = lambda x,y: x*y

print_operation_table(calk_1, 6, 6)
# list_rows = [x for x in range(1,r_num+1)]
# list_columns =[x for x in range(1, c_num+1)]
# print(f'len(list_rows) = {len(list_rows)}')
# print(f'len(list_columns) = {len(list_columns)}')
