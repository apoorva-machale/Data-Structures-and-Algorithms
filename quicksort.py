class Quicksort():
    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i+= 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        return i+1

    def q_sort(self, array, low, high):
        if (low < high):
            middle = self.partition(array, low, high)
            self.q_sort(array, low, middle-1)
            self.q_sort(array, middle+1, high)
    def print_list(self, array):
        for i in range(len(array)):
            print(array[i], end=" ")


object = Quicksort()
array = [8, 7, 2, 1, 0, 9, 6]
object.q_sort(array,0, len(array)-1)
print("Sorted array using quick sort")
object.print_list(array)