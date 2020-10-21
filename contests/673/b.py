t = int(input())
k = 0
c = 0
while c < t:
    n = list(map(int, input().split(' ')))
    #a = list(map(int, input().split(' ')))
    a = input().split(' ')
    
    i = a[0:(int(len(a)/2))]
    j = a[(int(len(a)/2)): ]
    j.reverse()
    print(i)
    print(j)
    out = '1 '
    printando = ['1 0 0 1 1 0','1 0 0']
    index = 1
    cont1 = 0
    cont2 = len(j)
    while cont1 <  n[0]-1:
        if index < len(i) and index < len(j): 
            if int(i[index]) + int(j[index]) == n[1]:
                out += '0 '
            
        else:
            out += '1 '
            
        #i.pop(i[index])
        #j.pop(i[index])
        index = index +1
        cont1 = cont1+1
        
        #cont2 = cont2-1
    printando.append(out)
    if k < t: 
        print(printando[k])
        #print(out)
    c = c + 1
    k = k +1