def factorial(n, acc=1):
    """Calculate the factorial of n using tail recursion."""
    if n == 0:
        return acc
    else:
        return factorial(n - 1, n * acc)

# Example usage
result = factorial(5)
print(f"Factorial of 5 is: {result}")  # Output: Factorial of 5 is: 120

# Test cases
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(6) == 720
assert factorial(7) == 5040
assert factorial(8) == 40320
assert factorial(9) == 362880
assert factorial(10) == 3628800