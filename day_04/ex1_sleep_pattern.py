events = []

for line in open('input.txt', 'r'):
    data = line[1:].split(']')
    events.append(data)

events.sort()

events = [(int(data[0][-2:]), data[1]) for data in events]

schedule = {}
current_guard = 0
asleep_since = 0

for event in events:
    if event[1].startswith(' Guard #'):
        current_guard = event[1].split(' ')[2]

        if current_guard not in schedule:
            schedule[current_guard] = [0 for i in range(60)]
    
    elif event[1] == ' falls asleep\n':
        asleep_since = event[0]
    
    elif event[1] == ' wakes up\n':
        for i in range(event[0]-asleep_since):
            schedule[current_guard][asleep_since+i] += 1
    
    else:
        print(f"Unknown event encountered: {event}")

sleepiest_guard = 0
nap_time = 0
amount = 0

for guard in schedule:
    if sum(schedule[guard]) > amount:
        sleepiest_guard = int(guard[1:])
        amount = sum(schedule[guard])

        record_minute = 0
        record_amount = 0

        for i in range(60):
            if schedule[guard][i] > record_amount:
                record_minute = i
                record_amount = schedule[guard][i]
        
        nap_time = record_minute
    
print(sleepiest_guard*nap_time)