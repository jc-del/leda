num = int(input())
coordinates =  input().split(' ')

if len(coordinates) == num:
    for i in range(len(coordinates)):
        min = 0
        max = 0
        if i == 0:
            min = int(coordinates[1]) - int(coordinates[0])
            max = int(coordinates[-1]) - int(coordinates[0])

        elif int(coordinates[i]) == int(coordinates[-1]):
            min = int(coordinates[-1]) - int(coordinates[-2])
            max = int(coordinates[-1]) - int(coordinates[0])

        else:
            min = int(coordinates[i]) - int(coordinates[i - 1])
            max = int(coordinates[-1]) - int(coordinates[i])

            if (int(coordinates[i + 1]) - int(coordinates[i])) < min:
                min = int(coordinates[i + 1]) - int(coordinates[i])
            if (int(coordinates[i]) - int(coordinates[0])) > max:
                max = int(coordinates[i]) - int(coordinates[0])

        print(str(min) + ' ' + str(max))