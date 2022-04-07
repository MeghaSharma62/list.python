#Given a list of numbers, write a Python program to count positive and
#negative numbers in a List.
#Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

list1 = [2, -7, 5, -64, -14]
i=0
count=0
count1=0
a=[]
b=[]
while i<len(list1):
       if list1[i] >0:
               count+=1
               a.append(list1[i])
       else:
                count1+=1
                b.append(list1[i])
       i+=1
print(count,a)
print(count1,b)

