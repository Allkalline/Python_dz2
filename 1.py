# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random
N = int(input('Введите количество монет: '))
count_one = 0
count_zero = 0
for i in range(N):
    x = random.randint(0,1)
    if x == 0:
        count_zero +=1
    else:
        count_one +=1
    print(x)
if count_one > count_zero:
    print('минимальное число монет, которые нужно перевернуть: ', count_zero)
    
else:
    print('минимальное число монет, которые нужно перевернуть: ', count_one)
