def print_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

print_pyramid(5)
print_pyramid(10)
print_pyramid(14)
print_pyramid(7)