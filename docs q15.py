# Our task is to print the element which occurs 3 consecutive times in a Python list.
# Example:
# Input: [4, 5, 5, 5, 3, 8]
# Output: 5
l=[4, 5, 5, 5, 3, 8]
i=0
count=0

while i<len(l):
        if l[i]==5:
                count+=1
                print(l[i])
                break
        i=i+1














# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output: 1, 22

a=[1, 1, 1, 64, 23, 64, 22, 22, 22]
i=0
c=0
while i<len(a):
        if a[i]==1 and a[i]==22:
                c+=1
                print(a[i])
                break
        i+=1


