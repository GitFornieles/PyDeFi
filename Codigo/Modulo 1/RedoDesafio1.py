def estas(arr1,arr2):
    arr3=[]
    if len(arr1)>len(arr2):
        for n in arr2:
            if arr1.count(n) and not arr3.count(n):
                arr3.append(n)
    else:
        for n in arr1:
            if arr2.count(n) and not arr3.count(n):
                arr3.append(n)
    return arr3

primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]

print(estas(primera,segunda))