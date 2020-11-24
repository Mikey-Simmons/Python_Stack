#1 Countdown

def countdown(x):
    my_list = []
    for num in range(x):
        my_list.append(num)
    my_list.reverse()
    print(my_list)

#2 
def print_and_return(x,y):
    print(x)
    return(y)

#3 
def first_plus_length(list):
    first_num = list[0]
    list_length = len(list)
    print(first_num + list_length)


the_list = [1,2,3]




#4Values Greater than Second - Write a function that accepts a list and creates a new list
# containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, 
# have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False

def greater_than_second(list):
    new_list = []
    print(list[2])
    for num in list:
        if num >= list[2]:
            new_list.append(num)
    print(new_list)       

#5 This Length, That Value - Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size,
#  and whose values are all the given value.

def this_length_that_value(length,value):
    new_list = []
    for num in range(length):
        new_list.append(value)
    print(new_list)
    
this_length_that_value(4,7)






