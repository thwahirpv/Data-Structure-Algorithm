class Selection_sort:
    # Using min and index funtion 
    def sort(self, arr):
        # Itrate over the array
        for i in range(len(arr)-1):
            # find the minimun value of the array (using slice arr[i:end]) 
            min_value = min(arr[i:])
            # find the index of the value 
            index = arr.index(min_value, i)
            # swap them
            arr[i], arr[index] = arr[index], arr[i]
        return arr
    
    # Without min and max function 
    def clean_sort(self, arr):
        # Iterate over the array
        for i in range(len(arr)-1):
            # Assume arr[i] is minimum value
            m_ind = i
            # Finding minimum value of this array
            for j in range(i+1, len(arr)):
                # If found any value less then arr[m_ind] take it as a minimum value
                if arr[j] < arr[m_ind]:
                    m_ind = j
            # Finally swap them
            if arr[i] != arr[m_ind]:
                arr[i], arr[m_ind] = arr[m_ind], arr[i]     
        return arr   
    
    def recursive_sort(self, arr, i=0):
        if i == len(arr)-1:
            return arr
        m_value = min(arr[i:])
        index = arr.index(m_value, i)
        if arr[i] != arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
        return self.recursive_sort(arr, i+1)
    
    def clean_recursive_sort(self, arr, i=0, j=1, min_ind=0):
        if i == len(arr)-1:
            return arr
        
        if j < len(arr):
            if arr[j] < arr[min_ind]:
                min_ind = j
            return self.clean_recursive_sort(arr, i, j+1, min_ind)
        else:
            if arr[i] != arr[min_ind]:
                arr[i], arr[min_ind] = arr[min_ind], arr[i]
            return self.clean_recursive_sort(arr, i+1, i+2, i+1)



ss = Selection_sort()
result = ss.clean_recursive_sort([34,54,23,23,3,43,23,54,65])
print(result)