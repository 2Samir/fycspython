print("hello world")

a = int(input("Enter no:"))
b = int(input("Enter no:"))
c = int(input("Enter no:"))

if a<b and a<c:
    print("a is samller")
elif b<c and b<a:
    print("b is samller")
elif a==b and b==c:
    print("all no are same")
else:
    print("c is samller")

print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a%b)
print(a//b)

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

for i in range(1,11):
    print(f"2 x {i} = {2*i}")
