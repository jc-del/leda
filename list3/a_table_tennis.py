from collections import deque
nums = input().split(' ')
powers = input().split(' ')
n = int(nums[0])
k = int(nums[1])
queue = []

    
for i in range(n):
    queue.append(int(powers[i]))



ans = queue[0]
s = 0
for j in range(1,n):
    if s >= k:
            #print(ans)
        break
        
    elif ans > queue[j]:
        s = s + 1
    else: 
        s = 1
        ans = queue[j]
print(ans)