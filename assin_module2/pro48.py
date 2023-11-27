#Write a Python program to find the maximum and minimum numbers from the specified decimal numbers. 

from decimal import Decimal

a=list(map(Decimal,'2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print("Maximum:",max(a))
print("Minimum:",min(a))