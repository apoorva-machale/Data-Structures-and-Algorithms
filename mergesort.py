class Mergesort:
    def m_sort(self, array):
        if len(array) >1:
            r = len(array) // 2
            
            L = array[:r]
            R = array[r:]
            self.m_sort(L)
            self.m_sort(R)

            i=j=k=0
            while i< len(L) and j< len(R):
                if L[i] < R[j]:
                    array[k] = L[i]
                    i+=1
                else:
                    array[k] = R[j]
                    j+=1
                k+=1
            
            while i < len(L):
                array[k] = L[i]
                i += 1
                k+=1
            while j < len(R):
                array[k] = R[j]
                j +=1
                k+=1


    def print_set(self,array):
        for i in array:
            print(i,end=" ")

object = Mergesort()
array_list = [6, 5, 12, 10, 9, 1]
object.m_sort(array_list)
print("Sorted array using Merge sort")
object.print_set(array_list)
