for line in open('input.txt'):
    string = line

reaction_found = True
c = 0

while reaction_found:
    c += 1
    print(f"Looping once more... (Loop {c})")
    reaction_found = False
    new_string = ""

    size = len(string)-1
    i = 0

    if size > 0:
        while i < size:
            char1 = string[i]
            char2 = string[i+1]

            if char1 == char1.upper() and char2 == char1.lower():
                reaction_found = True
                i += 1
            elif char1 == char1.lower() and char2 == char1.upper():
                reaction_found = True
                i += 1
            else:
                new_string += char1

            if i == size - 1:
                new_string += string[i+1]
        
            i += 1

        string = new_string

print(string)
print(len(string))