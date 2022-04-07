# Write a Python program to insert a specified element in a given list after every nth element.
# Original list:
# [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# Insert 20 in said list after every 4 th element:
# [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]


# a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]               
# list1=[]
# k=4
# i=0
# while i<len(a):
#         if i==k:
#                 list1.append(20)
#                 k+=4
#         list1.append(a[i])
#         i+=1
# print(list1)

        


a=[10,20,30,40]
b=[100,200,300,400]
i=0
d=[]
while i<len(a):
        s=a[i],b[-i]
        d.append(s)
        i+=1
print(d)
      



# a=[10,20,30,40]
# b=[2,3,4,5]
# i=0
# while i<len(a):
#         j=0  
#         while j<len(b):
#                 d=a[i]+b[j]
#         i+=1
# print(d)
















