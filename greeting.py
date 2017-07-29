name = input("what's your name?")
print("Nice to meet you", name)
color = input("what's your favorite color?")
print(color,"?","That's a nice color")
food = input("what's your favorite food?")
print(food,"sounds yummy")
def main():
    s1 = str(input("if you have to go?"))
    if (s1 == "no" or s1 =="No"):
        main()
    else:
        print("let's go")
main()