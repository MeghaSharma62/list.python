
# Write a Python program to iterate a given list cyclically on specific index position. 
# Original list:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Iterate the said list cyclically on specific index position 3 :
# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']





n=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i=0
a=(n[3:])
b=(n[:3])
print(a+b)