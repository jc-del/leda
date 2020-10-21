t = int(input())

c = 0
while c < t:
    the_floor = 0
    n_x = list(map(int, input().split(' ')))
    for x in range(1, 1000):
        if x * n_x[1] > n_x[0]+1 and  x-1 * n_x[1] < n_x[0]:
            print (x)  
            break

    c = c + 1