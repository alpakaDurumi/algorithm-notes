array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
	# if list has less than one element, return array
	if len(array) <= 1:
		return array

	pivot = array[0] # first element
	tail = array[1:] # elements except for pivot

	left_side = [x for x in tail if x <= pivot] # elements less than or equal pivot
	right_side = [x for x in tail if x > pivot] # elements greater than pivot

	return quick_sort(left_side) + [pivot] + quick_sort(right_side) # recursive call

print(quick_sort(array))