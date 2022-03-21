array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
	if start >= end: # start와 end가 같거나(원소가 1개) end가 더 왼쪽에 있는 경우
		return
	pivot = start # 첫 번째 원소를 피벗으로 지정
	left = start + 1
	right = end
	while left <= right: # 엇갈릴 때까지 반복
		while left <= end and array[left] <= array[pivot]:
			left += 1
			print(left)
		while right > start and array[right] >= array[pivot]:
			right -= 1
		if left > right: # 엇갈린 경우 작은 데이터와 피벗을 swap
			array[right], array[pivot] = array[pivot], array[right]
		else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 swap
			array[left], array[right] = array[right], array[left]
	quick_sort(array, start, right - 1) # 왼쪽 부분
	quick_sort(array, right + 1, end) # 오른쪽 부분

quick_sort(array, 0, len(array) - 1)
print(array)

# '=' in ln 10 (that between left and right)is need to change left and right when right == end
# For example in circumstance like 0 1 2 (4 3) 5 ...
# Unless '=' is exist, left and right are both 4, sorting is not occurred.
# And therefore in ln 4, infinite loop is occurred.