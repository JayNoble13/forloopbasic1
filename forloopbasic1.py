x = 0
for x in range(151):
    print(x)
    x += 1


total = 5
while total <= 1000:
    print(total)
    total = total + 5


def divisible_by(x,y):
    for total in range(0,100):
        if (total % 10) == 0:
            print("Coding Dojo")
        elif (total % 5) == 0:
            print("Coding")
        else:
            print(total)
divisible_by(0,100)

def oddintegers (x,y):
    for num in range (1, 500000):
        if num % 2 == 1:
            num -= 1
    print (sum(range(1,num,2))+num)
oddintegers(1,500000)

def countbyfour(x,y):
    for nums in range (0,2022):
        if nums % 4 == 0:
            print(nums - 4)
countbyfour(2018,0)