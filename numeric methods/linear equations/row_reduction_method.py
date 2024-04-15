columns = int(input("Enter number of equations (matrix columns): "))
rows = int(input("Enter number of variables (matrix rows): "))

print()
print("How to input equations: ")
print(" Examples with 4 equations and 4 variables (Four 3rd degree polynomials):")
print("  Eq1: 1+2x+3x²  Input:'1 2 3 0'")
print("  Eq2: 1-x²+3x³  Input:'1 -1 0 3'")
print("  Eq3: 4-3x³     Input:'4 0 0 -3'")
print("  Eq4: x         Input:'0 1 0 0'")
print("*Do not include the 's on the extremities of the input.")
print()

equations = []
equals = []

i = columns
while(i > 0):
    eq = input("Enter the terms of the (" + str(columns-i+1) + ") equation as shown in the examples: ")
    equations.append(eq.split(" "))
    i = i-1

print("Now you may input the value for each equation: ")
i = columns
while(i > 0):
    equals.append(input("Equation " + str(columns-i+1) + " equals to: "))
    i = i-1

print("Does this look correct?:")
j = rows
while j > 0:
    i = rows
    while i > 0:
        current = equations[rows-j][columns-i]
        if int(current) >= 0:
            if columns-i == columns-1:
                print(current + "", end='')
            else:
                print(current + "+", end='')
        else:
            print(current + "", end='')
        i = i - 1
    print("=", equals[rows-j])
    print()
    j = j - 1