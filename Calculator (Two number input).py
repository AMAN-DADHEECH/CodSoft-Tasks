print("THIS PROGRAM IS DESIGN FOR 2 NUMBER INPUT")
while True:
    print("+ --> ADDITION , - --> Subtractor , * --> multiplication , / --> True Devision , // --> Floor Devision , ** --> Exponent , % --> Modulus , Exit ---> (E or e)")
    o = input("Enter the operator -->")
    if o == 'E' or o == 'e':
        print(f"Exit Successfull")
        break
    else :
        a = eval(input("Enter the First number -->"))
        b = eval(input("Enter the Second number -->"))
        s=0
        if o == '+':
            s=a+b
            print(f"{a} {o} {b} == {s} The result is :{s}")
        elif o == '-':
            s=a-b
            print(f"{a} {o} {b} == {s} The result is :{s}")
        elif o == '*':
            s=a*b
            print(f"{a} {o} {b} == {s} The result is :{s}")
        elif o == '/' or o == '//':
            if b == 0:
                print("Can't Divide by zero(0)")
            elif o =='/':
                s=a/b
                print(f"{a} {o} {b} == {s} The result is :{s}")
            elif o == '//':
                s=a//b
                print(f"{a} {o} {b} == {s} The result is :{s}")
        elif o == '%':
            s=a%b
            print(f"{a} {o} {b} == {s} The result is :{s}")
        elif o == '**':
            s=a**b
            print(f"{a} {o} {b} == {s} The result is :{s}")
        else:
            print("Invalid Operand Input Try Again!!")

