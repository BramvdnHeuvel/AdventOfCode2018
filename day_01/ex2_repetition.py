sum = 0
sum_list = {sum}
number_found = False

while not number_found:
    for line in open('input.txt', 'r'):
        number = line.split('\n')[0]
        number = int(number)
        sum += number

        if sum in sum_list:
            print(sum)
            number_found = True
            break

        sum_list.add(sum)