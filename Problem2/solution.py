# Many online solutions to the original problem don't have support for 0's in the input array.
# The original problem statement says "integers," so they are technically allowed.

# Have not implemented the follow-up. Can be done simply with an O(n^2) solution, but will think on it.
def multiplyArray(array = []):
	totalValue = 1;
	numZeros = 0;
	for value in array:
		if value != 0:
			totalValue *= value
		else:
			numZeros += 1
	newArray = []
	for i in range(len(array)):
		if numZeros > 1:
			newArray.append(0)
		elif array[i] == 0:
			newArray.append(totalValue)
		elif numZeros == 1:
			newArray.append(0)
		else:
			arrayVal = array[i]
			newArray.append(totalValue / array[i])
	return newArray

def test():
    assert multiplyArray([3,2,1])==[2,3,6], "Given example 1"
    assert multiplyArray([1,2,3,4,5])==[120, 60, 40, 30, 24], "Given example 2"

    assert multiplyArray([1,2,0,4,5])==[0,0,40,0,0], "Test a single 0 in the array"
    assert multiplyArray([1,0,0,4,5])==[0,0,0,0,0], "Test multiple 0's in the array"
    assert multiplyArray([-1,-2,3,4,5])==[-120,-60,40,30,24], "Test negative integers"
    print("Tests Passed!")

test()