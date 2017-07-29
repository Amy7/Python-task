'''
def main():
    tf = int(input("how much the temperate in fahrenheit?"))
    tc = (tf - 32) * 5 / 9
    print("temperate in fahrenheit is", tf)
    print("temperate in celsius is", tc)
    option = input("do you want continue?")
    if (option == "yes" or option == "Yes" ):
        main()
    else:
        print("it's finished")

main()
'''

option = "yes"
while( option == "yes" or option =="Yes"):
    tf = int(input("how much the temperate in fahrenheit?"))
    tc = (tf - 32) * 5 / 9
    print("temperate in fahrenheit is", tf)
    print("temperate in celsius is", tc)
    option = str(input("do you want continue?"))