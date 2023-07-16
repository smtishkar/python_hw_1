# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: 
# “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input("Введите число для проверки: "))
# num = 89


MAX_VALE =100_000


def num_check (num, MAX_VALUE):
    count = 0
    for i in range(1,MAX_VALE):
        if num % i ==0:
            count +=1 

    return count


while num <=0 or num > MAX_VALE:
    print("введено не корретное число")
    num = int(input("Введите число для проверки: "))
if num >0 and num < MAX_VALE:
    if num_check(num, MAX_VALE) >2:
        print("число составное")
    else:
        print("число простое")
# else:
#     print("введено не корретное число")
# print(num_check(num, MAX_VALE))