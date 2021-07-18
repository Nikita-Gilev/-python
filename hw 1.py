
№1
a = 125
b = 100
x = a + b
print("a + b =", x)

№1
a = 1
b = 5
print("Переменные a и b - ", a, b)
string1 = input("Введите первую строку : ")
number1 = int(input("Введите первое число : "))
string2 = input("Введите вторую строку : ")
number2 = int(input("Введите второе число : "))
print("Введеные значения - %1s %5d %1s %5d" % (string1, number1, string2, number2))

№2
time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

№3

n = int(input("Введите число - "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn - %d" % total)

№4

n = abs(int(input("Введите целое положительное число ")))
max = n % 20
while n >= 1:
    n = n // 5
    if n % 5 > max:
        max = n % 5
    if n > 4:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break
        
 №5
 
profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила { (profit / costs) * 100: }")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers: }")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
    
    
 №6
 
 a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
