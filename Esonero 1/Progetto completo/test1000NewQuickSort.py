from demoSorting import *
if __name__ == "__main__":
    c=[0]*15
    start = time()
    inputType = 0  # 1 crescente, -1 decrescente, 0 random
    steps = 50000
    inputList = [None] * steps
    for i in range(0, steps):
        if inputType == 1:
            inputList[i] = i
        elif inputType == -1:
            inputList[i] = steps - i
        elif inputType == 0:
            inputList[i] = random.randint(0, steps)
        else:
            raise Exception("You used an invalid inputType parameter!")
        printSwitch.dumpOperations = False

    for j in range(1000):

        runningTime = sortingTest(inputList, nuovoQuicksort.newQuickSort, 1)

        if 0 < runningTime < 0.3:
            c[0]+=1
        if 0.3 <= runningTime < 0.5:
            c[1] += 1
        if 0.5 <= runningTime < 0.7:
            c[2] += 1
        if 0.7 <= runningTime < 0.75:
            c[3] += 1
        if 0.75 < runningTime < 0.8:
            c[4] += 1
        if 0.8 < runningTime < 0.85:
            c[5]+=1
        if 0.85 < runningTime < 0.9:
            c[6]+=1
        if 0.9 < runningTime < 0.95:
            c[7]+=1
        if 0.95 < runningTime < 1:
            c[8]+=1
        if 1 < runningTime < 1.05:
            c[9]+=1
        if 1.05 < runningTime < 1.1:
            c[10]+=1
        if 1.1 < runningTime < 1.15:
            c[11]+=1
        if 1.15 < runningTime < 1.2:
            c[12]+=1
        if 1.2 < runningTime < 1.25:
            c[13]+=1
        if 1.25 < runningTime < 1.3:
            c[14]+=1
    print(c)


