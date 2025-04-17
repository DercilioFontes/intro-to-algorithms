def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# Example usage
print(fib(0))  # Output: 0
print(fib(1))  # Output: 1
print(fib(2))  # Output: 1
print(fib(3))  # Output: 2
print(fib(4))  # Output: 3
print(fib(5))  # Output: 5
print(fib(6))  # Output: 8
print(fib(7))  # Output: 13
print(fib(8))  # Output: 21
print(fib(9))  # Output: 34
print(fib(10))  # Output: 55
print(fib(20))  # Output: 6765
print(fib(30))  # Output: 832040
print(fib(40))  # Output: 102334155
print(fib(50))  # Output: 12586269025
print(fib(100))  # Output: 354224848179261915075