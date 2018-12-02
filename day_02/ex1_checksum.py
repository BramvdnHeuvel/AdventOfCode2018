values_2 = 0
values_3 = 0

for line in open('input.txt', 'r'):
    string = line.split('\n')[0]
    letter_dict = {}

    for char in string:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1
    
    if 2 in letter_dict.values():
        values_2 += 1
    if 3 in letter_dict.values():
        values_3 += 1

checksum = values_2*values_3
print(checksum)