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


