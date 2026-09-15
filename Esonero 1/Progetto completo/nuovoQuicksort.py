from sampleMedianSelect import *
from Selection import quickSelectRand, quickSelectDet
from sorting.strutture.Stack import PilaArrayList as Stack

# NewQuickSort - RECURSIVE, with SampleMedianSelect, QuickSelect deterministic and non-deterministic

def newQuickSort(l, sel = 0):    # 0 sampleMedianSelect, 1 quickSelectRand, 2 quickSelectDet
    newRecursiveQuickSort(l, 0, len(l) - 1, sel)


def newRecursiveQuickSort(l, left, right, sel):

    if left >= right:
        return

    k = int(ceil((right-left+1)/2.0))

    if sel == 0:
        pivot = sampleMedianSelect(l[left:right+1], k, 10)
    elif sel == 1:
        pivot = quickSelectRand(l[left:right+1], k)
    elif sel == 2:
        pivot = quickSelectDet(l[left:right+1], k, 10)
    else:
        raise Exception("You used an invalid inputType parameter!")

    mid = partition(l, left, right, pivot)   # Ripartisce l'insieme rispetto a pivot e mi restituisce indice mid di
                                                # pivot nell'insieme con cui invocare la funzione ricorsivamente
    newRecursiveQuickSort(l, left, mid - 1, sel)
    newRecursiveQuickSort(l, mid + 1, right, sel)

# End of NewQuickSort - RECURSIVE, with SampleMedianSelect, QuickSelect deterministic and non-deterministic

# NewQuickSort - ITERATIVE, with SampleMedianSelect, QuickSelect deterministic and non-deterministic

def newQuickSortIter(l, sel = 0):     # 0 sampleMedianSelect, 1 quickSelectRand, 2 quickSelectDet
    newIterativeQuickSort(l, 0, len(l) - 1, sel)


def newIterativeQuickSort(l, left, right, sel):
    theStack = Stack()
    theStack.push(left)
    theStack.push(right)
    while not theStack.isEmpty():
        right = theStack.pop()
        left = theStack.pop()

        if right <= left:
            continue

        k = int(ceil((right - left + 1) / 2.0))

        if sel == 0:
            pivot = sampleMedianSelect(l[left:right + 1], k, 10)
        elif sel == 1:
            pivot = quickSelectRand(l[left:right + 1], k)
        elif sel == 2:
            pivot = quickSelectDet(l[left:right + 1], k, 10)
        else:
            raise Exception("You used an invalid inputType parameter!")

        mid = partition(l, left, right, pivot)    # Ripartisce l'insieme rispetto a pivot e mi restituisce indice mid
                                                     # di pivot nell'insieme
        theStack.push(left)
        theStack.push(mid - 1)

        theStack.push(mid + 1)
        theStack.push(right)

# End of NewQuickSort - ITERATIVE, with SampleMedianSelect, QuickSelect deterministic and non-deterministic

if __name__ == "__main__":
    # l = [4, 1234, 34, 566, 8, 2, 5346, 9, 3, 263, 7, 8, 3, 7, 57, 2, 43, 87, 845, 42]
    # l = [4, 1234, 34, 566, 8, 2, 5346, 9, 3, 263, 7, 8, 3, 7, 57, 2, 43, 87, 845, 42]*100
    # l = [1]
    # l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # l = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    l = [11, 12, 13, 14, 15, 16, 17]
    # l = []
    print(l)
    #newQuickSort(l, 1)
    newQuickSortIter(l, 2)


    # output should be: 2,2,3,3,4,7,7,8,8,8,34,42,43,57,87,263,566,845,1234,5346]
    print(l)



