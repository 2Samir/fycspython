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
