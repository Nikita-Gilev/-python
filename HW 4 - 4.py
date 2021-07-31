from itertools import permutations
from itertools import repeat
from itertools import combinations
my_list = [154, 2222, 2222, 334, 41, 1, 2, 3, 4, 88, 36, 37, 36, 77, 88]
new = [el for el in my_list if my_list.count(el)==1]
print(new)
