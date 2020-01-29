from structures.array import Array
from structures.stack import Stack

# Testing the Array data structure
print("TESTING ARRAYS ->")
arr = Array(5, int)

try:
    arr.insert(1, 'hi')
except TypeError as err:
    print(err)
try:
    arr.get(10)
except IndexError as err:
    print(err)

print(len(arr))
print(arr)

arr.insert(2, 2)
print(arr)

arr.delete(2)
print(arr)

arr.insert(2, 2)
print(arr)

for x in arr:
    print(x)
# Done testing the Array data structure

# Testing the Stack data structure
print("TESTING STACKS ->")
stack = Stack(str)

print('Checking Stack empty. Should be True.')
print(stack.isEmpty())
try:
    stack.push(1)
except TypeError as err:
    print(err)
try:
    stack.pop()
except IndexError as err:
    print(err)
try:
    stack.top()
except IndexError as err:
    print(err)

print(len(stack))
print(stack)

stack.push('hi0')
print(stack)

stack.push('hi1')
print(stack)

print(stack.top())

print('Checking Stack empty. Should be False.')
print(stack.isEmpty())

print(stack.pop())
print(stack.pop())
print(stack)

print('Checking Stack empty. Should be True.')
print(stack.isEmpty())
# Done testing the Stack data structure
