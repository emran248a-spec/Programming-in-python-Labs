# problem 01
print("\n for loop for sequence")
fruits = ["apple", "banana", "cherry", "mango"]
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

for ch in "Python":
    print(ch, end=" ")
print()

# problem 02
print("\n Countdown")
num = int(input("Enter a number: "))
while num >= 0:
    print(num)
    num -= 1

# problem 03
print("\nExponentiation")
base = float(input("Enter base: "))
exp = int(input("Enter exponent (integer): "))
result = 1
for _ in range(abs(exp)):
    result *= base
if exp < 0:
    result = 1 / result
print(f"{base} ^ {exp} = {result}")
print("Check with ** operator:", base ** exp)

# problem 04
print("\nSum of primes below 1000")
total = 0
for n in range(2, 1000):
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        total += n
print("Sum of primes below 1000 =", total)

# problem 05
print("\nFibonacci below N ")
N = int(input("Enter N: "))
a, b = 0, 1
while a < N:
    print(a, end=" ")
    a, b = b, a + b
print()



