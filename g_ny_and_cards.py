cards = input()

cont = 0
for l in cards:

    if l== 'a'or l== 'e'or l== 'i'or l== 'o'or l== 'u':
        cont = cont + 1
    elif l== '1'or l== '3'or l== '5'or l== '7'or l== '9':
        cont = cont + 1

print(cont)



