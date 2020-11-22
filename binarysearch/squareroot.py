n = 12
### Floor Value ###
left = 1
right = n
ans = right
while left<=right:
    
    mid = (left+right)//2
    square = mid**2 
    if square == n:
        ans = mid
        break
    if square < n:
        ans = mid
        left = mid+1
    else:
        right = mid-1
print(ans)

###  For float ###

square = mid = -1
left = 1
right = n
while abs(n-square) > pow(10, -6):
    mid = (left+right)/2
    square = mid**2
    if square < n:
        left = mid
    elif square > n:
        right = mid
    else:
        break
print(mid)

