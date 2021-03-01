import math
# a * x^2 + b * x + c = 0


def solve_equation(a, b, c):
    print(f"{a} * x^2 + {b} * x + {c} = 0")
    if(a == 0):
        if(b == 0):
            if(c == 0):
                print("x - any number")
            else:
                print("no solution")
        else:
            x = (-1) * c / b
            print("x =", x)
    else:
        discriminant = b ** 2 - 4 * a * c
        if(discriminant >= 0):
            x1 = ((-1) * b - math.sqrt(discriminant)) / (2 * a)
            x2 = ((-1) * b + math.sqrt(discriminant)) / (2 * a)
            print(f"x1 = {x1}\nx2 = {x2}")
        else:
            real = str(((-1) * b) / (2 * a))
            image = str(math.sqrt(abs(discriminant)) / (2 * a))
            print(f"x1 = {real} - i * {image}")
            print(f"x1 = {real} + i * {image}")
    print()


solve_equation(0, 0, 0)
solve_equation(0, 0, 1)
solve_equation(0, 1, 0)
solve_equation(0, 1, 1)
solve_equation(1, 0, 0)
solve_equation(1, 0, 1)
solve_equation(1, 1, 0)
solve_equation(1, 1, 1)
solve_equation(1, 2, 1)
solve_equation(1, -2, 1)
solve_equation(-1, -1, -1)
solve_equation(-1, -2, -1)
solve_equation(1, 2, 3)
solve_equation(-1, -2, -3)

