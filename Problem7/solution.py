#abcdefghijklmnopqrstuvwxyz

def numWaysToDecode(msg):
    msgLen = len(msg)
    if (msgLen == 0):
        return 1
    digitOne = int(msg[0])
    if (digitOne == 0):
        return 0
    if (msgLen == 1):
        return 1
    digitTwo = int(msg[1])
    if (digitOne <= 2 and digitTwo <= 6):
    	# In this case we can choose to interpret the pair of digits together or separately
        return numWaysToDecode(msg[1:]) + numWaysToDecode(msg[2:])
    else:
        return numWaysToDecode(msg[1:])




def test():
    assert numWaysToDecode('111')==3, "Given example"

    assert numWaysToDecode('')==1, "Only one way to decode the empty string, and it is another empty string"
    assert numWaysToDecode('1010')==1, "must be jj"
    assert numWaysToDecode('101022')==2, "first 4 chars must be `jj`, but last 2 are decodable 2 ways"
    assert numWaysToDecode('2222')==5, "decodable 5 ways (no pairs, 2 pairs of 22, or a pair starting at locations 0-2)"
    assert numWaysToDecode('101')==1, "`ja` only, as 0 is not decodable otherwise"
    print("Tests passed")

test()