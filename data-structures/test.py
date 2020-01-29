from structures.array import Array

# Testing the Array data structure
arr = Array(5, int)

try:
    arr.insert(1, "hi")
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