# Write a Python program to split a given list into specified sized chunks. 
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Split the said list into equal size 3
# [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]


a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
k=[]
l=[]
count=0
while i<len(a):
        if count==3:
                k.append(l)
                l=[]
                count=1
        else:
                count+=1
                l.append(a[i])
        i+=1
k.append(l)
print(k)

# n=[2,0,3,8,9,0,4,0,5]
# i=0
# b=[]
# k=[]
# while i<len(n):
#         if n[i]==0:
#                 b.append(n[i])
#         else:
#                 k.append(n[i])
#         i+=1
# i=0
# while i<len(b):
#         k.append(b[i])
#         i+=1
# print(k)