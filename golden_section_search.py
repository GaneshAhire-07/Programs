import math

def golden_section_search(f, a, b, tol=1e-5):
    # Golden ratio
    gr = (math.sqrt(5) + 1) / 2

    # Initial points
    c = b - (b - a) / gr
    d = a + (b - a) / gr

    # Iterative search
    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c

        # Recompute the points
        c = b - (b - a) / gr
        d = a + (b - a) / gr

    # The best point is in [a, b]
    return (b + a) / 2

# Define the function
def f(x):
    return x**3 - 3*x**2 + 7

# Interval [1, 3]
a = 1
b = 3

# Find the minimum
min_x = golden_section_search(f, a, b)
min_f = f(min_x)

print(f"The minimum value is approximately at x = {min_x:.5f}, f(x) = {min_f:.5f}")
