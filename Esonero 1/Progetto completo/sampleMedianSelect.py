from math import ceil
import random
from Selection import trivialSelect, partitionDet as partition



def sampleMedianSelect(l, k, minLen):
    if k <= 0 or k > len(l):
        return None
    return recursiveSampleMedianSelect(l, 0, len(l) - 1, k, minLen)

def recursiveSampleMedianSelect(l, left, right, k, minLen):

    # CASO BASE RICORSIONE

    if left == right:
        return l[left]

    if len(l) < minLen:
        med = trivialSelect(l[left: right + 1], k - left)
        return med

    # CASO GENERALE

    m = int(ceil((right-left)*0.01))
    randList = createRandomList(l, m, left, right+1)                # Creo sottoinsieme random di m elementi
    x = sampleMedianSelect(randList, int(ceil(m/2.0)), minLen)      # Prendo il mediano di randList e lo uso come pivot

    perno = partition(l, left, right, x)          # Indice del pivot x nell'insieme e partizione dell'insieme stesso

    posperno = perno + 1
    if posperno == k:
        return l[perno]
    if posperno > k:
        return recursiveSampleMedianSelect(l, left, perno - 1, k, minLen)
    else:
        return recursiveSampleMedianSelect(l, perno + 1, right, k, minLen)

def createRandomList(l, m, start, end):
    rand = random.sample(l[start:end], m)
    return rand

if __name__ == '__main__':
    basel = [5, 34, 26, 1, 4, 2, 17, 50, 41]
    k = 5
    l = list(basel)
    print(l)
    print(sampleMedianSelect(l, k, 3))
    print(l)
