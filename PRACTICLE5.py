num = int(input("check prime or not:"))
if num == 2:
    print("prime")

elif num>1:
    for i in range(2,num):
        if num%i==0:
            print("composite no")
            break
        else:
            print("prime no")
else:
    print("composite no")
