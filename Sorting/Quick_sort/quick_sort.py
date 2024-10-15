import random, statistics

class Quick_sort:
    def pivot_place_first(self, arr, first, last):
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

    
    def pivot_place_last(self, arr, first, last):
        pivot = arr[last]
        left = first
        right = last - 1
        while True:
            while left<=right and arr[left] <= pivot:
                left = left + 1
            while left<=right and arr[right] >= pivot:
                right = right - 1
            if left > right:
                break
            else:
                arr[left], arr[right] = arr[right], arr[left]
        arr[last], arr[left] = arr[left], arr[last]
        return left

    def pivot_place_random(self, arr, first, last):
        r_index = random.randint(first, last)
        # We assign the r_index last or first here i am assign last
        arr[r_index], arr[last] = arr[last], arr[r_index]
        pivot = arr[last]
        left = first
        right = last - 1
        while True:
            while left<=right and arr[left] <= pivot:
                left = left + 1
            while left<=right and arr[right] >= pivot:
                right = right - 1
            if left > right:
                break
            else:
                arr[left], arr[right] = arr[right], arr[left]
        arr[last], arr[left] = arr[left], arr[last]
        return left

    def pivot_place_median(self, arr, first, last):
        low = arr[first]
        mid = (first+last)//2
        heigh = arr[last]
        pivot = statistics.median([low, arr[mid], heigh])
        p_index = len(arr) - 1
    
        if pivot == low:
            p_index = first
        elif pivot == arr[mid]:
            p_index = mid
        else:
            p_index = last

        arr[p_index], arr[last] = arr[last], arr[p_index]
        pivot = arr[last]
        left = first 
        right = last - 1
        
        while True:
            while left<=right and arr[left] <= pivot:
                left = left + 1
            while left<=right and arr[right] >= pivot:
                right = right - 1
            
            if left > right:
                break
            else:
                arr[left], arr[right] = arr[right], arr[left]
        arr[last], arr[left] = arr[left], arr[last]
        return left        

    def quick_sort(self, arr, first, last):
        if first<last:
            p_index = self.pivot_place_median(arr, first, last)
            self.quick_sort(arr, first, p_index-1)
            self.quick_sort(arr, p_index+1, last)
        return arr
    

qs = Quick_sort()
arr = [45,3,23,43,63,22]
sorted_arr = qs.quick_sort(arr, 0, len(arr)-1)
print(sorted_arr)
        