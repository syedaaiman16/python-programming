a = 0
b = 1
# We have already two positions defined
count = 2
n = int(input("Enter the position you want to find in the Fibonacci series: "))

# The loop should run until count reaches n
while count <= n:
    temp = b
    b = a + b
    a = temp
    count += 1

print(f"The Fibonacci number at position {n} is {b}")
