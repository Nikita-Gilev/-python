import os, re

file_to_read_path = os.path.join('task6.txt')
def calculate_hours(calc_line: str):
    line_of_hours = re.sub(r'\D', ' ', calc_line)
    ttl_hours = 0
    for hour in line_of_hours.split():
        ttl_hours += float(hour)
    return ttl_hours


overall_subject_info = {}
with open(file_to_read_path, 'r', encoding='utf-8') as file_read:
    for line in file_read.readlines():
        listed_line = line.split(': ')
        overall_subject_info[listed_line[0]] = calculate_hours(listed_line[1])

print(f'Итого :\n {overall_subject_info}')
