# Задача 8: Требуется определить, можно ли 
# от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int (input('Введите число долек по горизонтали '))
m = int (input('Введите число долек по вертикали '))
k = int (input('Введите число долек, которое хотите отломить за один раз '))

if ((k % n == 0) or (k % m == 0)) and (k <= (n * m)):
    print('Получится')
else:
    print('Не получится')
