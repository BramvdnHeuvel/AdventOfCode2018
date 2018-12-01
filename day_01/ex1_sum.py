open_file = open('input.txt', 'r')

sum = 0

for line in open_file:
    number = line.split('\n')[0]
    number = int(number)
    sum += number

print(sum)