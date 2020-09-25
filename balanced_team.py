n = int(input())
a = list(map(int, input().split(' ')))

if n == len(a):
    l = sorted(a)
    result = 0
    sum1 = 0
    print(l)
    for i in range(0, n-1):
        j = i+1
        '''
        if i<j :
            if int(l[j]) - int(l[i]) < 5:
                    #print('ooo summm' + str(sum1))
                    sum1 = sum1 + 1
                    j = j + 1
            else:
                   # print('ooo summm' + str(sum1))
                    sum1 = sum1 - 1
                    i = i + 1
        '''

        for j in range(2, n-1, 1):
            if int(l[j]) - int(l[i]) <= 5:
                sum1 = sum1 + 1
                j = j + 1
            else:
                sum1 = sum1 - 1
        i = i + 1
        result = max(sum1, result)
    print (result)