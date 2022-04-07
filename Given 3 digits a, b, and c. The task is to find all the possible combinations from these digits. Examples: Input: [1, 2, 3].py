# Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
# Examples:
# a=(input("Enter the number:"))
# b=(input("enter the number:"))
# c=(input("enter the number:"))
# i=0
# d=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if (i!=j and j!=k and i!=k):
#                 print(a[i],a[j],a[k])
#             k+=1
#         j+=1
#     i+=1
# Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
# Examples:
# a=(input("Enter the number:"))
# b=(input("enter the number:"))
# c=(input("enter the number:"))
# i=0
# d=[]
# while i<len(a):
#         if d!=a[i]:
#             j=0
#             while j<len(b):
#                 if d!=b[i]:
#                     k=0      
#                     while k<len(c):
#                         if d!=c[i]:
#                       



a=[11000,1200,30000,500000,12600]
i=0
b=[]
while i<len(a):
    while a[i]>0:
        if a[i]%10!=0:
            b.append(a[i])
            break
        a[i]//=10
    i+=1
print(b)
        





# a=(input("Enter first number:"))
# b=(input("Enter second number:"))
# c=(input("Enter third number:"))
# d=[]
# i=0
# while i<len(a):
#     if i!=a[i]:
#         d.append(a)
#         print(d[i])
#         i+=1
#         j=0
#         while j<len(b):
#             if j!=b[i]:
#                 d.append(b)
#                 print(b[j])
#                 j+=1
#                 k=0
#                 while k<len(c):
#                     if k!=c[i]:
#                         d.append(c)
#                         print(d[k])
#                     k+=1



# d.append(b)
# d.append(c)

# for i in range(0,3):
#     for j in range(0,3):
#         for k in range(0,3):
#             if(i!=j&j!=k&k!=i):
#                 print(d[i],d[j],d[k])
                        