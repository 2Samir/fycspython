marks = float(input("Enter your no: "))


if marks <=100:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 55:
        print("Grade c")
    elif marks >= 35:
        print("pass")
    else:
        print("Fail")
else:
    print("not vailid")
