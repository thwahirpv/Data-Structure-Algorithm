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
    

bs = Bubble_sort()
sorted_arr = bs.sort([34,54,66,4,23,43,2,6,0,23])
print(sorted_arr)                