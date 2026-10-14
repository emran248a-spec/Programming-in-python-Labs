#solution 3
import math

# problem 01
print("Swapping")
a = input("Enter a: ")
b = input("Enter b: ")
print("Before swap: a =", a, ", b =", b)
a, b = b, a          
print("After swap:  a =", a, ", b =", b)

# problem 02
print("\nDistance between two points")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance =", round(d, 4))

# problem 03
print("\nEven/Odd")
n = int(input("Enter an integer: "))
if n % 2 == 0:
    print(n, "is Even")
else:
    print(n, "is Odd")

# problem 04
print("\nVowel")
ch = input("Enter a character: ")
if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single letter.")
elif ch.lower() in "aeiou":
    print(ch, "is a vowel")
else:
    print(ch, "is not a vowel")

# problem 05
print("\nGrade")
marks = float(input("Enter marks (0-100): "))
if marks < 0 or marks > 100:
    print("Invalid marks!")
elif marks >= 90:
    print("Grade: A+  (CGPA 4.00)")
elif marks >= 85:
    print("Grade: A   (CGPA 3.75)")
elif marks >= 80:
    print("Grade: B+  (CGPA 3.50)")
elif marks >= 75:
    print("Grade: B   (CGPA 3.25)")
elif marks >= 70:
    print("Grade: C+  (CGPA 3.00)")
elif marks >= 65:
    print("Grade: C   (CGPA 2.75)")
elif marks >= 60:
    print("Grade: D+  (CGPA 2.50)")
elif marks >= 50:
    print("Grade: D   (CGPA 2.25)")
else:
    print("Grade: F   (CGPA 0.00)")


#solution 4


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
