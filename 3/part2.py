def overweightBits():
    with open('input.txt', 'r') as r:
        bins = r.read().splitlines()
        bytelen = len(bins[0])
        zeros = 0
        ones = 0
        overweight = []
        for i in range(0, bytelen):
            for row in bins:
                if row[i] == '0':
                    zeros += 1
                if row[i] == '1':
                    ones += 1
            if zeros > ones:
                overweight.append(0)
            if ones > zeros:
                overweight.append(1)
            zeros = 0 
            ones = 0
        return(overweight)


filterByWeight(overweightBits())
