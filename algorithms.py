class Algoritmhs:
    @staticmethod
    def selectionSort(array):
        size = len(array)
        for ind in range(size):
            min_index = ind
            for j in range(ind + 1, size):
                if array[j] < array[min_index]:
                    min_index = j
            (array[ind], array[min_index]) = (array[min_index], array[ind])

    @staticmethod
    def insertionSort(array):

        for step in range(1, len(array)):
            key = array[step]
            j = step - 1
                 
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key

    @staticmethod
    def bubbleSort(array):  
        for i in range(0,len(array)-1):  
            for j in range(len(array)-1):  
                if(array[j]>array[j+1]):  
                    temp = array[j]  
                    array[j] = array[j+1]  
                    array[j+1] = temp  
        return array  
    
    
    @staticmethod
    def mergeSort(array):
        if len(array) > 1:
            r = len(array)//2
            L = array[:r]
            M = array[r:]
            
            Algoritmhs.mergeSort(L)
            Algoritmhs.mergeSort(M)

            i = j = k = 0

            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1

            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1



    @staticmethod
    def partition (array, start, end):
        pivot = array[end]
        i = start
        for j in range(start, end):
            if array[j] <= pivot:
                array[j], array[i] = array[i], array[j]
                i = i + 1
        array[i], array[end] = array[end], array[i]
        return i
    
    @staticmethod
    def quickSort(array, left = 0, right = None):
        if right is None:
            right = len(array) - 1
        if left < right:
            index = Algoritmhs.partition(array, left, right)
            Algoritmhs.quickSort(array, left, index - 1)
            Algoritmhs.quickSort(array, index + 1, right)

