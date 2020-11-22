a = [23, 27, 2, 3, 9, 12, 19, 20, 21]
n = len(a)
left = 0
right = n-1
pivot = -1

while right-left>1:
	
	mid = (left+right)//2

	if a[mid] < a[left]:
		right = mid

	elif a[mid] > a[right]:
		left = mid

	else:
		pivot = left
		break

if pivot == -1:

	if a[left] < a[right]:
		pivot = left

	else:
		pivot = right

print(pivot)