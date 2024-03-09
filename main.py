def bubble_sort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array

arr=[6,8,3,1,1,8,3,4]
arr=bubble_sort(arr)
print(arr)
