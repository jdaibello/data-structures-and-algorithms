import array

my_array = array.array('i', [1, 2, 3, 4])
print(my_array)

my_array.insert(4, 5)
print(my_array)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(my_array, 5))
