import math

print("Enter the Quadratic Equation: \n")

a = int(input("Enter the cofficient value of X^2 : "))
b = int(input("Enter the cofficient value of X : "))
c = int(input("Enter the  value of C(constant) : "))

root1=root2 = 0

d = (b*b)-4*a*c
if d<0:
    print("Roots of this equation is imaginary!")
elif d == 0:
    root1 = -b/(2*a)
    print(f"Roots of this equation are equals : {root1}")
else:
    root1 = -b + (math.sqrt(d)/(2*a))

    root2 = -b - (math.sqrt(d)/(2*a))

    print(f"Roots of this equations are Root1 : {root1:.2f} , Root2 : {root2:.2f}")