
#task is to find maximum and minimum elements in the array
arr = [1, 4, 3, 5, 8, 6]

min_element = arr[0]
max_element = arr[0]

for i in range(1, len(arr)):
    if arr[i] < min_element:
        min_element = arr[i]
    if arr[i] > max_element:
        max_element = arr[i]

print([min_element, max_element])

#task is to find and return kth smallest element in the given array

arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
arr.sort()
print(arr[k-1])

#to return the union of arrays in any order given as a[] b[]
def union_arrays(a, b):
    return list(set(a) | set(b))

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

result = union_arrays(a, b)
result

#given an array arr[]. the task is to find the largest element
arr = [1, 8, 7, 56, 90]
print(max(arr))
 
#given an array of integers arr[] ,you have to find the reverse
def reverseArray(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [1, 4, 3, 2, 6, 5]
reverseArray(arr)
print(arr)