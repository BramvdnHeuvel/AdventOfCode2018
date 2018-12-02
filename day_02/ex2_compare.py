def find_deviators(file_name):
    for line1 in open(file_name, 'r'):
        for line2 in open(file_name, 'r'):
            
            string1 = line1.split('\n')[0]
            string2 = line2.split('\n')[0]

            deviation = 0

            for chart in zip(string1, string2):
                char1 = chart[0]
                char2 = chart[1]

                if char1 != char2:
                    deviation += 1

                    if deviation > 1:
                        break
            
            if deviation == 1:
                return (string1, string2)

matches = find_deviators('input.txt')

for chart in zip(matches[0], matches[1]):
    if chart[0] == chart[1]:
        print(chart[0], end='')