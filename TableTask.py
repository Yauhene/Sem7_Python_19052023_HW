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
#r_num = 6
#c_num = 6

def print_operation_table(operation, num_rows=6, num_columns=6):
    r_num = num_rows
    c_num = num_columns
    list_rows = [x for x in range(1,r_num+1)]
    list_columns =[x for x in range(1, c_num+1)]
    
    #for i in range(0,c_num): # вернуть на место 2
    for i in range(0,r_num):
        if i==0:
            for x in list_columns:
                print("{:6d}".format(x), end='')
            #print()
        else: 
            print("{:6d}".format(list_rows[i]), ' ', end='') 
            
            #print(f'c_num = {c_num}')

            for j in range(1,c_num):
            #for j in range(1,r_num): #вернуть на место!
                #print(f"i = {i}, j = {j}, calk_1(list_columns[j],list_rows[i] = {calk_1(list_columns[j],list_rows[i])}", end='')  
                if type(calk_1(list_rows[i], list_columns[j])) != int:
                    print("{:5.1f}".format(calk_1(list_columns[j],list_rows[i])), end='')   
                else:        
                    print("{:6d}".format(calk_1(list_columns[j],list_rows[i])), end='')          

        print()
        
calk_1 = lambda x,y: x*y

print_operation_table(calk_1, 6, 6)

print('////////////////////////////////////////////////////////////////////')
print("Прошу прощения за корявость вывода в консоль.")
print("Косяк вызван попыткой хоть как-то сохранить вид таблицы при варианте 'x/y'.")
print('Возиться не стал просто чтобы не городить уж совсем лишнего.')
print('////////////////////////////////////////////////////////////////////')
print()