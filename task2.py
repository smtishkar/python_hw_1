# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


a = 4           # Длина первой стороны треугольника
b = 4           # Длина второй стороны треугольника
c = 4           # Длина третьей стороны треугольника

check_1 = a + b
check_2 = a + c
check_3 = c + b

# c = 20        #Проверка что код работает  
if check_1 < c or check_2 < b or check_3 < a:
    print("треугольник не существует")
else:
    if a == b and b == c:
        print("Треугольник равносторонний")
    elif a == b or b == c or a == c:
        print("Треугольник равнобедренный")
    else: 
        print("Треугольник разносторонний")