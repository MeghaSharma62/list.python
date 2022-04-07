# Write a Python program to remove the last N number of elements from a given list. 
# Original lists:
# Remove the last 3 elements from the said list:


# n=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# i=0
# # count=0
# b=[]
# while i<len(n):
#         c=n[:-3]
#         # b.append(c)
#         i+=1
# print(c)
        

# Remove the last 5 elements from the said list:
# n=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
# i=0
# count=0
# while i<len(n):
#         c=n[:-5]
#         i+=1
# print(c)


# a=int(input("Enter the number"))
# n=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# i=0
# h=[]
# while i<len(n)-a:
#         h.append(n[i])
#         i+=1
# print(h)
        


# Remove the last 1 element from the said list:
# a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]
# i=0
# count=0
# while i<len(a):
#         c=a[:-1]
#         i+=1
# print(c)



# odd number,even number

# i=1
# a=[]
# b=[]
# while i<=20:
#         n=int(input("Enter the number"))
#         if i%2==0:
#                 a.append(i)
#         # print(a,"even number")
#         else:
#                 b.append(i)
#         # print(b,"odd number")
#         i+=1
# print(a)
# print(b)


# i=1
# j=10
# while i<=10 and j>=1:
#     print(i,j)
#     j-=1
#     i=i+1


# all tables print

# a=int(input("enter the number"))
# i=1
# while i<=a:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",j*i)
#         j+=1
#     print()
#     i+=1


# a=int(input("enter the number"))
# b=int(input("enter the number"))
# i=0
# while i<=15:
#         print(a,"*",i,"=",a*i)
#         i+=1


a=[[1,2,3],[4,5,6]]
i=0
b=[]
sum=0
while i<len(a):
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            sum+=a[i][j]
            j+=1
        i+=1
print(b)
print(sum)


