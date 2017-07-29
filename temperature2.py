tc = 0
print("TC","\t\t","TF")
while( tc<=100):
    tf = tc * 9/5 + 32
    if(tc < 100):
        print(tc,"\t\t",tf)
    else:
        print(tc,"\t",tf)
    tc+=5
