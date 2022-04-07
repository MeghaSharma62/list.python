# Write a Python program to convert a given list of strings into list of lists. 
# Original list of strings:
# ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]


# a="husna"
# i=0
# b=[]
# while i<len(a):
#         j=0
#         while j<len(a[i]):
#                 b.append(a[i])
#                 j+=1
#         i+=1
# print(b)

# i=0
# b=[]
# max=0
# min=0
# while i<=10:
#         n=int(input("Enter the number"))
#         b.append(n)
#         if b[i]>max:
#                 max=b[i]
#                 print(max)
#         if n[i]<min:
#                 min=b[i]
#                 print(min)
#         i+=1


# nums=[1,2,3,4]
# i=0
# sum=0
# b=[]
# while i<len(nums):
#         sum+=nums[i]
#         b.append(sum)
#         i+=1
# print(b)


# a=[1,"m",2,"e",3,"g"]
# i=0
# b=[]
# while i<len(a):
#         if type (a[i])!=int:
#                 b.append(a[i])
#         i+=1
# print(b) 


a=["banana","cherry","apple","watermelon","mango"]
i=0
b=[]
count=a
while i<len(a):
        j=0
        while j<len(a):
                if count==a:
                        b.append(a[i][j])
                j+=1
        i+=1
print(b)

# name=["snowball","chewy","bubbles","gruff"]
# animal=["cat","dog","fish","goat"]
# age=["1","2","3","4"]
# i=0
# b=[]
# while i<len(name):
#         d=name[i]+"the"+animal[i]+"is"+age[i]
#         # b.append(d)
#         i+=1
#         print(d)



# n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
# i=0
# b=[]
# while i<len(n):
#         if n[i]>12 and n[i]<18:
#                 b.append(n[i])
#         i+=1
# print(b)

# a=int(input("enter te number"))
# b=(a//1)%10
# c=(a//10)%10
# d=(a//100)%10
# rev=b*100+c*10+d*1
# print(rev)
















