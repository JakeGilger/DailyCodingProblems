class XORNode:
    def __init__(self, val, both=0):
        self.val = val
        self.both = both
        pointers.append(self)

class XORList:
    def __init__(self):
        initialNode = XORNode(None)
        self.head = initialNode
        self.tail = initialNode

    def add(self, elem):
        # Get the first and last element, and create a new node with an XOR of their refs.
        head = self.head
        tail = self.tail
        newNode = XORNode(elem, get_pointer(head) ^ get_pointer(tail))
        newNodePtr = get_pointer(newNode)
        # Now that we have a new node, scrub head and tail's knowledge of each other.
        head.both = head.both ^ get_pointer(tail)
        tail.both = tail.both ^ get_pointer(head)
        # Add new node's pointer to both head and tail.
        head.both = head.both ^ newNodePtr
        tail.both = tail.both ^ newNodePtr
        # Fix list's tail ref
        self.tail = newNode

    def get(self, index):
        currPtr = get_pointer(self.head)
        prevPtr = get_pointer(self.tail)
        counter = 0
        while (counter <= index):
            prevPtr, currPtr = currPtr, prevPtr ^ dereference_pointer(currPtr).both
            counter += 1
        return dereference_pointer(currPtr)





# Inefficient impl to translate nodes to ints and vice versa; this was supposedly provided in the problem statement.
# Only added here so test will work.
pointers = []
def get_pointer(node):
    for i in range(len(pointers)):
        if (pointers[i] == node):
            return i
    print("Pointer not found for node: " + str(node))
    return -1

def dereference_pointer(address):
    return pointers[address]






def test():
    # First test ptr deref impl
    testPtr1 = XORNode('a')
    testPtr2 = XORNode('b')
    assert dereference_pointer(get_pointer(testPtr1))==testPtr1
    assert dereference_pointer(get_pointer(testPtr2))==testPtr2

    myList = XORList()
    myList.add("3")
    myList.add("5")
    myList.add("7")
    myList.add("12")
    assert myList.get(0).val=="3"
    assert myList.get(2).val=="7"
    assert myList.get(1).val=="5"
    assert myList.get(3).val=="12"
    print("Tests passed")

test()