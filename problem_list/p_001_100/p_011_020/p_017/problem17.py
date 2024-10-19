import math
from pprint import pprint
import numpy as np

count = 0

number_names = {
    0: {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    },

    1: {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    },

    2: {
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    },

    3: {
        100: 'hundred'
    },

    4: {
        1000: 'thousand'
    }
}
number_names_len = {}

for digit_class in number_names.keys():
    number_names_len[digit_class] = {}
    for number, number_name in number_names[digit_class].items():
        number_names_len[digit_class][number] = len(number_name)

number_class_len = {}
for digit_class in number_names_len.keys():
    number_class_len[digit_class] = sum(number_names_len[digit_class].values())

pprint(number_names_len)
print()
print(number_class_len)

a = number_class_len

# 0 - 9
count = a[0]
# 10 - 19
count += a[1]
# 20 - 99
count += 10 * a[2]   # 10x twenty, 10x thirty ...
count += 8 * a[0]    # twenty + one, two, three ...
to_hundred = count
# 100 - 999
count += 9 * a[3] * 100     # 900x hundred
count += a[0] * 100         # 100x one, 100x two
count += 9 * to_hundred
count += 891 * len('and')
# 1000
count += a[4] + len('one')

print(count)