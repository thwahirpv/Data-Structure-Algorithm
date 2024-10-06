class Bubble_sort:
    def sort(self, arr):
        # outer loop for itrating over the array and hold each of them
        for i in range(len(arr)-1): 
            # Inner loop for itrating over the array and comparing each of them with arr[j] and arr[j+1]
            swap = False
            for j in range(len(arr)-1-i):
                # check arr[j] > arr[j+1] for assending if it is desending arr[j] < arr[j+1] if the condition is right 
                # we will swap it between. if it's not right continue the exicution. 
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap = True 
                # print(arr)
            # using this condition we can reduse the useless itration.
            if swap is False:
                return arr
            # print()
        return arr
    
    def recursive_sort(self, arr, i=0, j=0):
        # It's base case exit. if the condition is meet its means the array is sorted.
        if i == len(arr)-1:
            return arr
        
        # This condition is like inner loop itrating over the array and compare each of them.
        if j < len(arr)-1-i:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            return self.recursive_sort(arr, i, j+1)
        else:
            # It's like outer loop for holding the each element in array.
            return self.recursive_sort(arr, i+1, j=0)
    

bs = Bubble_sort()
sorted_arr = bs.recursive_sort([34,54,66,4,23,43,2,6,0,23])
print(sorted_arr)                