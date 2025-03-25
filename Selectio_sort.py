def selection_sort(arr):
	n = len(arr)
	for i in range(n - 1):
    	min_index = i  
    	for j in range(i + 1, n):  
        	if arr[j] < arr[min_index]:
                min_index = j
    	arr[i], arr[min_index] = arr[min_index], arr[i]
	return arr

arr = [64, 25, 12, 22, 11]
print("Original Array:", arr)
sorted_array = selection_sort(arr)
print("Sorted Array:", sorted_array)



OUTPUT:
Original Array: [64, 25, 12, 22, 11]
Sorted Array: [11, 12, 22, 25, 64]
