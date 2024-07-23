
def bubble_sort(array):
    for i in range((n := len(array))-1):
        already_sorted = False
        for j in range(n - 1 - i):
            if array[j] > array[1 + j]:
                array[j], array[1 + j] = array[1 + j], array[j]
                already_sorted = True
        if not already_sorted:
            break
    
    print(f"sorted array: {array}")


my_array = [3, 45, 1, 4, 56, 100, 21, 12, 33]
bubble_sort(my_array)