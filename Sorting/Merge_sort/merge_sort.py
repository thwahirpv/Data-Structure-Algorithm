class Merge_sort:
    def sort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            left_arr = arr[:mid]
            right_arr = arr[mid:]
            self.sort(left_arr)
            self.sort(right_arr)
        
            i = 0
            j = 0
            k = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i = i + 1
                    k = k + 1
                else:
                    arr[k] = right_arr[j]
                    j = j + 1
                    k = k + 1

            while i < len(left_arr):
                arr[k] = left_arr[i]
                i = i + 1
                k = k + 1
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j = j + 1
                k = k + 1
            
        return arr

ms = Merge_sort()
sorted_arr = ms.sort([34,5,4,23,55,75,21,11])
print(sorted_arr)

        