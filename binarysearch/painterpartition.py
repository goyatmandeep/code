def possible(boards, painters, time):
    ''' Returns True if it is possibe to paint 
        all boards in 'time' units using given 'painters'
    '''
    if painters < 1:
        return False
    temp = 0
    for i in range(len(boards)):
        if boards[i] > time:
            return False
        if temp+boards[i] > time:
            temp = boards[i]
            painters -= 1
            if painters == 0:
                return False
        else:
            temp += boards[i]
    return True
    
boards = [10, 20, 15, 30, 24, 35, 28, 15, 10]
painters = 4

left = max(boards)
right = sum(boards)
minimum_time = right

while left <= right:
    mid = (left+right)//2
    if possible(boards, painters, mid):
        minimum_time = mid
        right = mid-1
    else:
        left = mid+1
print(minimum_time)
