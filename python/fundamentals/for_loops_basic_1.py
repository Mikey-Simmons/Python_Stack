for num in range(151):
    print(num)

for num in range(5,1001,5):
    print(num)

for num in range(1,100,1):
    if num % 5 == 0:
        print("Coding")
    if num % 10 == 0:
        print("Coding Dojo")
    else:
        print(num)

sum = 0 

for num in range(0,500000,1):
    if num % 2 == 0:
        continue
    else:
        sum = sum + num

print(sum)      

    

for num in range(2018,0,-4):
    print(num)


lowNum = 1
highNum = 100
mult = 20


for num in range(lowNum,highNum,1):
    if num % 20 ==0:
        print(num)