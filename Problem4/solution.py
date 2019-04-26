def validValue(x, arrayLen):
    return x <= arrayLen and x >= 1

def firstMissingNaturalNumber(array = []):
    arrayLen = len(array)
    elem = 0
    tempValue = 0
    nextValue = 0

    for i in range(arrayLen):
        tempValue = array[i]
        if validValue(tempValue, arrayLen):
            # Follow the chain
            nextValue = array[tempValue - 1]
            while tempValue != nextValue:
                array[tempValue - 1] = tempValue
                tempValue = nextValue
                if validValue(nextValue, arrayLen):
                    nextValue = array[tempValue - 1]
                else:
                    break


    # Look for a gap in the "sorted" list
    for i in range(arrayLen):
        if array[i] != i + 1:
            return i + 1
    return arrayLen + 1

def test():
    assert firstMissingNaturalNumber([3, 4, -1, 1])==2, "Given example 1"
    assert firstMissingNaturalNumber([1, 2, 0])==3, "Given example 2"


    assert firstMissingNaturalNumber([3,2,1])==4, "Reversed list"
    assert firstMissingNaturalNumber([1,2,3,4,5])==6, "Trivial sorted list"
    assert firstMissingNaturalNumber([1,2,0,4,5])==3, "Missing an intermediate number"
    assert firstMissingNaturalNumber([2,-1,-2,4,1,4,5])==3, "Some negative integers and duplicates"
    print("Tests Passed!")

test()