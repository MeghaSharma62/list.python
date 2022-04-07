# input :
# 1 1 2 3 4 5 1 2
# 1
# Output :
# 2 3 4 5 2
# Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1.
# After removing the item, the output list is [2, 3, 4, 5, 2]


# i=0
# b=[]
# while i<=4:
#         n= int(input("Enter the number:"))
#         if n!= 1:
#             b.append(n)
#         i+=1
# print(b)


# n=[1,1,2,5,4,2,1]
# i=0
# b=[]
# while i<len(n):
#         if n[i]!=1:
#                 b.append(n[i])
#         i+=1
# print(b)

# def display_person(*args):
#     for i in args:
#         print(i)

# display_person(age="25")


# def fun1(name, age):
#     print(name, age)
# fun1("Emma",age=23)

# def fun1(**kwargs):
#     fun1(25, 75, 55)
# fun1(10, 20)


# def fun1(name, age=20):
#     print(name, age)

# fun1('Emma', 25)


# def fun1(name, age=20):
#     print(name, age)

# fun1('Emma', 25)


# def add(a, b):
#     return a+5, b+5

# result = add(3, 2)
# print(result)

# def display(**kwargs):
#     for i in kwargs:
#         print(i)

# display(emp="Kelly", salary=9000)


# def fun1(num):
#     return num + 25
# print(num)
# fun1(5)
# print(num)


# a=[1,2,3,4,5]
# i=0
# b=[]
# j=1
# while i<len(a):
#     if a[i]==a[-j]:
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)


# def my():
#     a=int(input("Enter the number"))
#     b=int(input("Enter the number"))
#     c=a+b
#     if c>15 and c<20:
#         return 20
#     else:
#         return c
# # a=int(input("enter the number"))
# # b=int(input("enter the number"))
# print(my())

a=["abc","aba","1231","shiva"]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]==a[i][j]:
            print("yes")