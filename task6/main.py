'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
    001001 -> yes

'''

n = int (input('Введите 6-тизначный номер вашего билета '))
if ((n // 100000) + ((n // 10000) % 10) + ((n // 1000) % 10)) == (((n % 1000) // 100) + ((n % 100) // 10) + ((n % 10))):
    print('У вас счастливый билет')

else:
    print('У вас обычный билет')