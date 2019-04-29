def cons(a, b):
	def pair(f):
		return f(a, b)
	return pair

def car(p):
	def func(a, b):
		return a
	return p(func)

def cdr(p):
	def func(a, b):
		return b
	return p(func)

def test():
    assert car(cons(3, 4))==3, "Given example 1"
    assert cdr(cons(3, 4))==4, "Given example 2"
    print("Tests passed!")

test();