class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(tree):
	if tree == None:
		return None
	nodeTuple = (tree.val, serialize(tree.left), serialize(tree.right))
	return str(nodeTuple)





def deserialize(treeString):
	return eval(treeString)

def test():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    print("Test passed")

test()