#mutliplication table with no repeated multiplication
for i in range (1,11): #doesn't include 10 in this interation
    for j in range (i,11): #when i is 2, j will be 2 meaning it will not run 1*2 again and move straight to 2*2
        print(f"{i} X {j} = {i*j}")

#only additions but computes (e.g.) 2**3

a = int(input("Enter a positive integer for a: "))
b = int(input("Enter a positive integer for b: "))

# Initialize the result to 1 (since any number raised to 0 is 1)
result = 1

# Loop b times to compute a**b
for i in range(b):
    # Simulate multiplication: result * a using only additions.
    product = 0
    for j in range(a):
        product += result  # Add 'result' a times
    result = product  # Update result with the new product

print(f"{a} raised to the power {b} is: {result}")

# Read an integer from the user
num = int(input("Enter an integer: "))

# Convert the number to a string for easy reversal
num_str = str(num)

# Check if the string is the same forwards and backwards
if num_str == num_str[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
