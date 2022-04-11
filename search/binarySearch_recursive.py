# 이진 탐색 (재귀)
def binary_search(array, target, start, end):
	if start > end:
		# None은 다른 언어에서의 Null에 해당한다
		return None
	mid = (start + end) // 2
	# 찾으면 인덱스 반환
	if array[mid] == target:
		return mid
	# target이 위치한 쪽을 재귀적으로 호출하여 확인
	elif array[mid] > target:
		return binary_search(array, target, start, mid - 1)
	else:
		return binary_search(array, target, mid + 1, end)

# 원소의 개수, target, array 입력받기 
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
	print("원소가 존재하지 않습니다.")
else:
	print(result + 1)