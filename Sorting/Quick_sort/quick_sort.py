class Quick_sort:
    def pivot_place(self, arr, first, last):
        pivot = arr[first]
        left = first + 1
        right = last
        while True:
            while left<=right and arr[left] <= pivot:
                left = left+1
            while left<=right and arr[right] >= pivot:
                right = right-1
            
            if left > right:
                break
            else:
                arr[left], arr[right] = arr[right], arr[left]
        arr[first], arr[right] = arr[right], arr[first]
        return right

    def quick_sort(self, arr, first, last):
        if first<last:
            p_index = self.pivot_place(arr, first, last)
            self.quick_sort(arr, first, p_index-1)
            self.quick_sort(arr, p_index+1, last)
        return arr
    

qs = Quick_sort()
arr = [45,3,23,43,63,22]
sorted_arr = qs.quick_sort(arr, 0, len(arr)-1)
print(sorted_arr)
        