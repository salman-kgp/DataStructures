'''Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in array. Elements for which no greater element exist, consider next greater element as -1.'''

from basic.stack import Stack
def print_nge(num_list):
	if len(num_list)==0:
		return
	stack = Stack()
	stack.push(num_list[0])
	for i in range(1,len(num_list)):
		curr_elem = num_list[i]
		while  not stack.isEmpty() and stack.peek()<curr_elem:
			print curr_elem
			stack.pop()
		stack.push(curr_elem)
	while not stack.isEmpty():
		stack.pop()
		print -1

	return


print_nge([1,2,3])
print_nge([1,3,2,4,5,2,7])




