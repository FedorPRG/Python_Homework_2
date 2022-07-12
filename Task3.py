#Задать список из n чисел последовательности (1+1n)^n и вывести на экран их сумму

n=int(input('Введите число n='))
rezult=0
for i in range(1,n+1):
    rezult+=(1+1/i)**i
    print(f'{i}->{rezult}')

