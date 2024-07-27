import timeit

class Quicksort:
    def __init__(self):
        self.array = []

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quicksort(self, array, low=0, high=None):
        if high is None:
            high = len(array) - 1

        if low < high:
            pivot_index = self.partition(array, low, high)
            self.quicksort(array, low, pivot_index - 1)
            self.quicksort(array, pivot_index + 1, high)

    def sort(self, array):
        self.quicksort(array)
        print(f"Sorted array: {array}")

def sort_and_measure():
    sorter = Quicksort()
    my_array = [64, 8, 90, 8, 6, 0, 7, 13, 45, 65]
    sorter.sort(my_array)
    return my_array

execution_time = timeit.timeit(sort_and_measure, number=1)

print(f"Time taken to sort: {execution_time:.6f} seconds")


