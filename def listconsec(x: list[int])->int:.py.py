def listconsec(x: list[int])->int:
    if len(x) < 2:
        return 0
    count = 0
    if x[i] == x[i] + 1:
        count += 1

    else:
        count = 0

    return count +listconsec(x[1:])


    print(listconsec([1,2,3,4,5,6,7,8,9,10]))
    
    