def gammaRate():
    with open('input.txt', 'r') as r:
        bins = r.read().splitlines()
        bytelen = len(bins[0])
        zeros = 0
        ones = 0
        newbyte = ''
        for i in range(0, bytelen):
            for bin in bins:
                bit = str(bin)[i]
                if bit == '0':
                    zeros += 1
                if bit == '1':
                    ones += 1
            if zeros > ones:
                newbyte += '0'
            if zeros < ones:
                newbyte += '1'
            zeros = 0
            ones = 0
        r.close()
        return(newbyte)

def epsilonRate():
    with open('input.txt', 'r') as r:
        bins = r.read().splitlines()
        bytelen = len(bins[0])
        zeros = 0
        ones = 0
        newbyte = ''
        for i in range(0, bytelen):
            for bin in bins:
                bit = str(bin)[i]
                if bit == '1':
                    zeros += 1
                if bit == '0':
                    ones += 1
            if zeros > ones:
                newbyte += '0'
            if zeros < ones:
                newbyte += '1'
            zeros = 0
            ones = 0
        r.close()
        return(newbyte)

def powerCalc():
    powerConsumption = int(epsilonRate(), 2) * int(gammaRate(), 2)
    print(powerConsumption)
powerCalc()