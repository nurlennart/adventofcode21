def partOne():
    numbers = []

    with open('1.txt', 'r') as r:
        for line in r.readlines():
            numbers.append(int(line))

    c = 0
    for i in range(0, len(numbers)):
        if numbers[i] > numbers[i-1]:
            c += 1
    print(c) 

def partTwo():
    numbers = []
    sums = []
    c = 0

    with open('1.txt', 'r') as r:
        for line in r.readlines():
            numbers.append(int(line))

    for i in range(0, len(numbers)):
        try:
            sums.append(numbers[i] + numbers[i+1] + numbers[i+2])
        except:
            continue
        i += 2
    
    for i in range(0, len(sums)):
        if sums[i] > sums[i-1]:
            c += 1
    print(c)



partTwo()
