# def print_star_pattern(n):
#     for i in range(1, n + 1):
#         # Print leading spaces
#         for j in range(n - i):
#             print(" ", end="")
#         # Print stars
#         for k in range(2 * i - 1):
#             print("*", end="")
#         # Move to the next line
#         print()

# # Set the value of n
# n = 3
# print_star_pattern(n)

def print_star_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if n - i < j < n + i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Set the value of n
n = 3
print_star_pattern(n)

