# Factorial (7) = 7x6x5x4x3x2x1 = ....
# Factorial (6) = 6x5x4x3x2x1 = ....
# Factorial (5) = 5x4x3x2x1 = ....
# Factorial (0) = 1 

# Factorial (n) = n * Factorial (n-1)

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
            # 5 x factorial (4)
            # 5 x 4 x factorial (3)
            # 5 x 4 x 3 x factorial (2)
            # 5 x 4 x 3 x 2 x factorial (1)
            # 5 x 4 x 3 x 2 x 1


#Quick Quiz - Write a program to print for fibonacci sequence
# fn = 0
# f1 = 1
# f2 = f1 = f0
# fn= f(n-1)+f(n-2)