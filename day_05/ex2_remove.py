def import_polymer(file_name='input.txt'):
    for line in open(file_name):
        return line

def create_short_polymer(polymer=import_polymer()):
    string = polymer

    reaction_found = True
    c = 0

    while reaction_found:
        c += 1
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

    return string

print("Creating short polymer...")
string = create_short_polymer()
print("Short polymer created!")

polymer_list = []

for removed_char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    print(f"Creating short list without character {removed_char}...")
    new_string = ''

    for char in string:
        if char not in [removed_char, removed_char.upper()]:
            new_string += char
    
    polymer_list.append(len(create_short_polymer(new_string)))

print(min(polymer_list))