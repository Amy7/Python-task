import random
number = random.randint(1,10)
print(number)
n = 3

while(n):
    try:
        guess = int(input(("please guess the number:")))
        while(guess > 10 or guess < 0):
            guess = int(input((" please input your number from 1 to 10")))
        n -= 1
        if(guess == number):
            print("congratulation!")
        elif(guess-number==1 or guess-number==-1):
            print("it's hot")
        elif(guess-number==2 or guess-number==-2):
            print("it's warm")

            print("This is the except: please input your number from 1 to 10")
        else:
            print("it's cold")
    except:
        print("This is the except: please input your number from 1 to 10")

