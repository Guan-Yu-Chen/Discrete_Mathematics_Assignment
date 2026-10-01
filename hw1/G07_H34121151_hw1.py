# This code can run without a problem.
# 
# How to run: 
# 1. Input the file that contains 2 lines, where line 1 is an integer n; and line 2 contains n+1 real numbers a[0], a[1],..., a[n]
# 2. It will print out a text like f(x)= a[0] + a[1] x + a[2] x^2 + ... + a[n] x^n 
# 3. It will ask the user to input a value of x, say, b. Then it calculates and outputs f(b)
# 4. It repeats step 3, unless b=0, which prints out f(0) and STOP
# 
# This code is written by G07_H34121151  email H34121151@gs.ncku.edu.tw, on 2025/03/02

from decimal import Decimal

def print_polynomial_func(deg, coefficients):
    func = ""
    for i in range(deg+1):
        if coefficients[i] == 0:
            continue

        op = " +" if coefficients[i] > 0 else " -"

        if coefficients[i] == int(coefficients[i]):
            c = " " + str(abs(int(coefficients[i])))
        else:
            c = " " + str(abs(coefficients[i]))

        if i == 0:
            x_term = ""
        elif i == 1:
            x_term = " x"
        else:
            x_term = f" x^{i}"

        func += op + c + x_term

    if func[:2] == " +":
        func = func[2:]
    print(f"f(x)={func}")

def calc_poly_func(x, deg, coefficients):
    sum = 0
    for i in range(deg+1):
        sum += Decimal(str(coefficients[i])) * x ** i
    return sum


filename = input("Enter a text filename: ")
with open(file=filename, mode='r', encoding='utf8') as myfile:
    deg = int(myfile.readline())
    coefficients = [float(c) for c in myfile.readline().split()]
    
print_polynomial_func(deg, coefficients)

while True:
    x = Decimal(input("\nInput the value of x: "))
    if x == 0:
        print(f"f(0)= {coefficients[0]}")
        print(f"STOP!")
        break
    else:
        print(f"f({x})= {calc_poly_func(x, deg, coefficients)}")
