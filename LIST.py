# Домашка работа со списками
from random import randint

# 1 ЗАДАНИЕ
# Сгенерируем список со случайными значениями от 1 до 200
print('TASK-1 ↓')
print('========================================================')

first_task_list = [randint(1, 200) for i in range(20)]

for i in range(len(first_task_list)):
    if first_task_list[i] > 100:
        print(first_task_list[i], end=' ')
print()
print('These number are bigger then 100')
print('========================================================')
print()

print('TASK-2 ↓')
print('========================================================')
# 2 ЗАДАНИЕ

# так же создадим рандомный список
my_second_task_result = []
second_task_list = [randint(1, 200) for i in range(20)]
for i in range(len(second_task_list)):
    if second_task_list[i] > 100:
        my_second_task_result.extend([second_task_list[i]])
print(my_second_task_result)
print('These number in new list are bigger then 100')
print('========================================================')
print()

print('TASK-3 ↓')
print('========================================================')
# 3 ЗАДАНИЕ

# создадим список с помощью рандома с (0 - 4) элементов в списке.


third_task_list = [randint(1, 200) for i in range(randint(0, 4))]

if len(third_task_list) <= 2:
    third_task_list.append(0)
    print('Mеньше или равно 2:')
else:
    new_el = third_task_list[-1] + third_task_list[-2]
    third_task_list.append(new_el)
    print('Больше 2:')
print(third_task_list)

print('========================================================')
print()

print('TASK-4 ↓')
print('========================================================')
# 4 ЗАДАНИЕ
# создадим и список и индек с помощью рандома

fourth_task_list = [randint(1, 200) for i in range(20)]
print(f'1) {fourth_task_list} - Оригинальный список')
k_index = randint(0, 20)
print(f'2) {k_index} - Случайный индекс')
fourth_task_list = fourth_task_list[0:k_index] + fourth_task_list[k_index + 1:] + fourth_task_list[k_index:k_index+1]
print(f'3) {fourth_task_list}- Элемент под выбранным индексом перемещен вправо')
fourth_task_list.pop()
print(f'4) {fourth_task_list}- Элемент под выбранным индексом удален из списка')
print('========================================================')






