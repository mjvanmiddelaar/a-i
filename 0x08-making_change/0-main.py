#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__("0-making_change_db").makeChange

print(makeChange([1,4,5],8))
print(makeChange([1,3,5,7,9],14))
print(makeChange([1,3,5,7,9],15))
print(makeChange([1,3,5,7,9],16))
print(makeChange([1,3,5,7,9],17))
print(makeChange([1,3,5,7,9],18))
print(makeChange([1,3,5,7,9],19))
print(makeChange([1,5,9],19))
print(makeChange([1,5,8],19))
print(makeChange([1,5,7],19))
print(makeChange([1,5,20],19))
print(makeChange([2,3,4,5,6],200))
print(makeChange([44],33))

