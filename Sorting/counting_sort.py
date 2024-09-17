class Counting:
    def count_sort(self, array):
        array_size = len(array)
        output = [0] * array_size
        count = [0] * 10

        for i in range(0, array_size):
            count[array[i]] += 1
        
        for i in range(1, 10):
            count[i] += count[i-1]
        
        for i in range(len(array)):
            output[count[array[i]] - 1] = array[i]
            count[array[i]] -= 1
        
        for i in range(0, array_size):
            array[i] = output[i]
        

    def print_list(self, array):
        for i in range(len(array)):
            print(array[i], end=" ")

obj = Counting()
array  = [4, 2, 2, 8, 3, 3, 1]
obj.count_sort(array)
print("Array sorted using counting sort ")
obj.print_list(array)