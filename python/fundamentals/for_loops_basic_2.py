# 1) Biggie Size - Given a list, write a function that
#  changes all positive numbers in the list to "big".

def biggie_size(list):
    for num in range(len(list)):
        if num > 0:
            list[num] = 'big'
    

    print(list)

# 2)
#Given a list of numbers, create a function to replace
#  the last value with the number of positive values.
#  (Note that zero is not considered to be a positive number).

def count_postives(list):
    counter = 0
    for num in list:
        if num > 0:
            counter = counter +1
    list[len(list)-1] = counter
    print(list)

# 3)Sum Total - Create a function that takes a list
#  and returns the sum of all the values in the list

def sum_total(list):
    sum = 0
    for num in list:
        sum = sum + num
    return(sum)

# 4) Average - Create a function that takes a list and returns the average of all the values.x

def get_average(list):
    sum = 0
    average = 0
    for num in list:
        sum = sum + num
    average = sum/len(list)
    return(average)

# 5) Length - Create a function that takes a list and returns the length of the list

def get_length(list):
    length = 0

    for num in list:
       length = length + 1
    return(length)


# 6) Minimum - Create a function that takes a list of numbers and returns the minimum value in the list.
#  If the list is empty, have the function return False.

def get_min(list):
    min = list[0]
    for num in list:
        if num < min:
            min = num
    return(min)

# 7) maximum

def get_max(list):
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return(max)

# 8) Ultimate Analysis Create a function that takes a
#  list and returns a dictionary that has the sumTotal,
#  average, minimum, maximum and length of the list

def get_ultimate_analysis(list):
    sum = 0
    length = 0
    average = 0
    min = list[0]
    max = list[0]
    for num in list:
        sum = sum +num
        length = length + 1
        if num < min:
            min = num
        if num > max:
            max = num 
    average = sum/len(list)
    return(f"sum: {sum}, length: {length}, avg: {average}, min: {min}, max: {max}")


# 9) reverse list

def reverse_list(list):
    list.reverse()
    print(list)

reverse_list([1,2,3])