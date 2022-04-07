# Write a code that works for any list, it should give two sums as outputs,
# one is the sum of odd numbers present in the list and the other is the sum of
# even numbers present in the list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
a=[]
b=[]
while i<len(elements):
        if elements[i]%2==0:
                sum=sum+elements[i]
                a.append(elements[i])
        else:
                sum1=sum1+elements[i]
                b.append(elements[i])       
        i+=1
print(a,sum)
print(b,sum1)        



# sum of odd numbers and even number in a list
# elements=[2,4,5,9]
# i=0
# sum=0
# sum1=0
# a=[]
# b=[]
# while i<len(elements):
#         if elements[i]%2==0:
#                 sum=sum+elements[i]
                
#                 a.append(elements[i])
#         else:
#                 sum1=sum1+elements[i]
        
#                 b.append(elements[i])       
#         i+=1

# print(sum)
# print(sum1)        
        