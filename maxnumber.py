n = int(input("how many nunbers do you want input?"))
mylist =[]
while(n):
    numbers = int(input("please input numbers:"))
    mylist.append(numbers)
    n-=1
print(mylist)
mylist.sort()
print(mylist)
min = mylist.pop(0)
max = mylist.pop()
print("the smallest number is",min)
print("the maximum number is",max)