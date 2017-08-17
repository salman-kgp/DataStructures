
from basic import stack



def isBalanced(inp,check_symbol=('(',')')):
	first_symbol = check_symbol[0]
	second_symbol  = check_symbol[1]
	search = stack.Stack()

	for c in inp:
		if c == first_symbol:
			search.push(c)
		elif c ==  second_symbol:
			if search.isEmpty():
				return False
			elif search.pop() == first_symbol :
				continue
			else:
				return False

	return True

print isBalanced('())')