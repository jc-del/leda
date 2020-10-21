# errado porque eu nao entendi o que se pedia nao 
t = int(input())

c = 0
while c < t:
        i = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))
        copy = a
        spell = 0
        n = i[0] 
        k = i[1]
        aux_1 = 0
        aux_2 = 0
        cont = 1
        
        while cont <= k:
            
            for i in range(1, len(a)):
                aux_1 = aux_1 + 1
                print('auxiliar 1: ' + str(aux_1))
                cont = cont+1 
        cont = 1
        while cont <= k:
            
            for j in range(len(a), 0, -1):
                aux_2 = aux_2 + 1
                print('auxiliar 2: ' + str(aux_2))
                cont = cont+1
        spell = max(aux_1, aux_2) 
        print(spell)
        c = c + 1