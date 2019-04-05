def numk(array, k):
	hashedVals = {}
	for elem in array:
		if (k - elem) in hashedVals:
			return True
		hashedVals.update({elem: True})
	return False

def test():
    assert numk([10, 15, 3, 7], 17)==True, "Given example"

    assert numk([10, -1, 12, 5], 9)==True, "Negative numbers"
    print("Tests Passed!")

test()