class Insertion_sort:
    def sort(self, arr):
        # This forloop iteration start with one and end with length of the array.
        # right side of the array consider as a unsorted part. 
        # As the every iteration unsorted part will decrease.
        for index in range(1, len(arr)):
            # It's part of unsorted list
            # The current variable hold a value from unsorted list
            current = arr[index] 
            # It's current index
            pos = index
            # This use to compare the sorted and unsorted part
            # Like pos-1 its means sorted part it's from left part of the array
            # The iteration go until the 0 of the sorted part
            # We check the current value from the unssorted part less then the current value from the sorted part.
            while current < arr[pos-1] and pos>0:
                # its will assing the value to right part of the array
                arr[pos] = arr[pos-1]
                pos = pos-1
            # Here we are assign finally if the while work or not
            arr[pos] = current
        return arr
    
    def recursive_sort(self, arr, index=1, pos=1):
        if index == len(arr):
            return arr
        
        if index == pos:
            self.current = arr[index]

        # With using while loop
        # while current > arr[pos-1] and pos>0:
        #     arr[pos] = arr[pos-1]
        #     pos = pos -1
       
        # Without using while loop
        if self.current < arr[pos-1] and pos>0:
            arr[pos] = arr[pos-1]
            return self.recursive_sort(arr, index, pos-1)
        
        arr[pos] = self.current
        return self.recursive_sort(arr, index+1, pos=index+1)



in_sort = Insertion_sort()
sorted_arr = in_sort.recursive_sort([34,23,2,12,5,23,1])
print(sorted_arr)