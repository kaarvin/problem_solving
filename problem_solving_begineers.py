# -*- coding: utf-8 -*-
"""problem_solving_begineers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VBTc2xE4xXbbg87zTvFyW4q_ddhJj-K_

# **problem solving begin**
"""

"""You are provided with a number check whether its odd or even.

Print "Odd" or "Even" for the corresponding cases.

Note: In case of a decimal, Round off to nearest integer and then find the output. Incase the input is zero, print "Zero".

Input Description:
A number is provided as the input.

Output Description:
Find out whether the number is odd or even. Print "Odd" or "Even" for the corresponding cases. Note: In case of a decimal, Round off to nearest integer and then find the output. In case the input is zero, print "Zero".

Sample Input :
2
Sample Output :
Even

a = float(input())
a = round(a)


if a == 0:
    print("Zero")

elif a % 2 == 0:
    print("Even")

else:
    print("Odd")

"""You are given with a number A i.e. the temperature in Celcius. Write a program to convert this into Fahrenheit.

Note: In case of decimal values, round-off to two decimal places.

Input Description:
A number is provided in Celcius as the input of the program.

Output Description:
The output shall be the temperature converted into Fahrenheit corresponding to the input value print up to two decimal places and round off if required.

Sample Input :
12
Sample Output :
53.60

celsius = float(input())


fahrenheit = (celsius * 9/5) + 32


fahrenheit = round(fahrenheit, 2)


print(fahrenheit)

"""You are given A = Length of a rectangle & B = breadth of a rectangle. Find its area “C”.

(A and B are natural numbers)

Input Description:
The inputs are two natural numbers representing the length and the breadth of a rectangle.

Output Description:
Find the area of the rectangle formed by the provided input. Round off the answer to the first decimal place if required.

Sample Input :
2
3
Sample Output :
6

length = float(input())
breadth = float(input())

area = length * breadth

area = round(area, 1)

print(area)

"""You are given a number A in Kilometers. Convert this into B: Meters and C: Centi-Metres.

Input Description:
A number "A" representing some distance in kilometer is provided to you as the input.

Output Description:
Convert and print this value in meters and centimeters.

Sample Input :
2
Sample Output :
2000
200000

kilometers = float(input())


meters = kilometers * 1000
centimeters = kilometers * 100000


print(int(meters))
print(int(centimeters))

"""You are given with a number "N", find its cube.

Input Description:
A positive integer is provided.

Output Description:
Find the cube of the number.

Sample Input :
2
Sample Output :
8

a = int(input())
cube = a ** 3
print(cube)

"""# Input
A = int(input())
B = int(input())
C = int(input())

# Find the largest number
if A >= B and A >= C:
    largest = A
elif B >= A and B >= C:
    largest = B
else:
    largest = C

# Output
print(largest)

A = int(input())
B = int(input())
C = int(input())
if A >= B and A >= C:
    largest = A
elif B >= A and B >= C:
    largest = B
else:
    largest = C
print(largest)

"""You are provided with two numbers. Find and print the smaller number.

Input Description:
You are provided with two numbers as input.

Output Description:
Print the small number out of the two numbers.

Sample Input :
23 1
Sample Output :
1

numbers = input().split()
number1 = int(numbers[0])
number2 = int(numbers[1])
if number1 < number2:
    smaller = number1
else:
    smaller = number2
print(smaller)

"""You are provided with a number "N", Find the Nth term of the series: 1, 4, 9, 16, 25, 36, 49, 64, 81, .......

(Print "Error" if N = negative value and 0 if N = 0).

Input Description:
An integer N is provided to you as the input.

Output Description:
Find the Nth term in the provided series.

Sample Input :
18
Sample Output :
324

N = int(input())
if N <= 0:
    print("Error")
else:
    Nth_term = N ** 2
    print(Nth_term)







