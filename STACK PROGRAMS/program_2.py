
# prepare stack using collection class

from collections import deque

stack_var = deque()

print("datatype of stack_var:",type(stack_var))

print("---------- add first value 10 -----------")
stack_var.append(10)
print("value after adding 10:",stack_var)

print("---------- add first value 20 -----------")
stack_var.append(20)
print("value after adding 20:",stack_var)

print("---------- add first value 30 -----------")
stack_var.append(30)
print("value after adding 30:",stack_var)

print("---------- remove last value -----------")
stack_var.pop()
print("value after removing last value:",stack_var)