import os

file_path = os.path.join('sal.txt')
file = open(file_path, 'r', encoding='utf-8')
lines = file.readlines()

sum = 0
for row in lines:
    line = row.split()

    if (float(line[1]) < 20000):
        print(f'{line[0]} Имеет оклад менее 20000руб 00коп')

    sum += float(line[1])

print(f'В среднем зароботок: {sum} руб')

file.close()
