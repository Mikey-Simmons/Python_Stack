def PrintMaxOfArray(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i 
    print(max)
PrintMaxOfArray([1,10,2,1])