# Find the First Maximum, Second maximum, Third maximum number from the List.

# n=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# max=0
# max1=0
# max2=0
# i=0
# while i<len(n):
#         if n[i]>max:
#                 max=n[i]
#         i+=1
# i=0
# while i<len(n):
#         if n[i]>max1 and n[i]!=max:
#                 max1=n[i]
#         i+=1
# i=0
# while i<len(n):
#         if n[i]>max2 and n[i]!=max and n[i]!=max1:
#                 max2=n[i]
#         i+=1
# print(max,max1,max2)

# n=int(input("Enter the number:"))
# i=n
# sum=0
# while i>0:
#         sum=sum+i%10
#         i=i//10
# print(sum)
# if i%sum==0:
#         print("Harshad number")
# else:
#         print("not")

# num=int(input("Enter the number"))
# rev=0
# while num>0:
#         rev=(num%10)
#         num//=10
#         print(rev,end="")
#         rev+=1
        

# a=4
# b=3
# if a<b:
#         print("yes")
# if a>b:
#         print("yes")
# else:
#         print("no")


# num=int(input("enter the number"))
# if num==num:
#         print(-num)
# else:
#         print(num)

# num=int(input("Enter the number"))
# i=1
# count=0
# while i<=num:
#         if num%i==0:
#                 count+=1
#         i+=1
# if count==2:
#         print("yes")
# else:
#         print("no")




# n=int(input("Enter the number"))
# fac=1
# while n>0:
#         fac=fac*n
#         n=n-1
# print(fac)


# n=int(input("Enter the number"))
# i=2
# while i<=n:
#         j=0
#         while j<=10:
#                 print(i,"*",j,"=",j*i)
#                 j+=1
#         print()
#         i+=1


# a=[100,200,300,400]
# b=[10,20,30,40]
# i=0
# # d=[]
# while i<len(a):
#         j=0
#         while j<len(a):
#                 s=a[i],b[-j]
#                 # d.append(s)
#                 # print((a[i]),(b[-j]))
#                 j+=1
#         i+=1
# print(d)



# a=[100,200,300,400]
# b=[10,20,30,40]
# i=0
# while i<len(a):
#         j=1
#         while j<=len(b):
#                 print([a[i],b[-j]],end=" ")
#                 j=j+1
#                 i=i+1
        
# a=2+5j
# b=33.50
# print(a+b)
# a=[11000,1200,30000,500000,12600]
# i=0
# b=[]
# while i<len(a):
#     while a[i]>0:
#         if a[i]%10!=0:
#             b.append(a[i])
#             break
#         a[i]//=10
#     i+=1
# print(b)
        


# n = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# i=0
# g=[]
# while i<len(n):
#         j=0
#         count=0
#         while j<len(n):
#                 if n[i]==n[j]:
#                         count=count+1
#                 j=j+1
#         if count>2:
#                 if n[i] not in g:
#                         g.append(n[i])
#         i=i+1 
# print(g)


# a="Pratiksha"
# i=0
# c=5
# b=[]
# while i<len(a):
#         b.append(a[i])
#         b.append(c)
#         c+=5
#         i+=1
# print(b)


# a=["Ankita","Anjali","Megha"]
# i=1
# d=[]
# while i<=len(a):
#         b=a[-i]
#         j=1
#         while j<=len(a):
#                 c=a[-i][-j]  
#                 j+=1
#         d.append(c)
#         i+=1
# print(d)



# a=["ankita","anjali","megha"]
# i=1
# b=[]
# while i<len(a):
#         j=0
#         while j<len(a[i]):
#                 d=(a[i][j])+1
#                 b.append(d)
#                 j+=1
#         i+=1
# print(d)

# a=[1,2,1,3,4,2,1,3,2]
# number=[1,1,2,2,3,3,4]
# i=0
# d=[]
# count=0
# while i<len(a):
#         j=0
#         while j<len(a):
#                 b=a[i]
#                 c=a[j]
#                 if (a[i],[j])==number:
#                         d.append([b,c])
#                         j+=1
#                 i+=1
# print(a)


# a=[1,2,1,3,4,2,1,3,2]
# i=0
# count=0
# d=[]
# while i<len(a):
#         if count(a[i])==2:
#                 d.append(a[i])
#                 count+=1
#                 # j+=1
#         i+=1
# print(d)


# a=[1,2,1,3,4,2,1,3,2]
# i=0
# count=0
# d=[]
# while i<len(a):
#         if a[i]==1:
#                 count+=1
#                 if count==2:
#                         d.append(a[i])
#         if a[i]==2:
#                 count+=1
#                 if count==2:
#                         d.append(a[i])
#         i+=1
# print(d,count)



# a=[1,2,1,3,4,2,1,3,2]
# b=[]
# i=0
# while i<len(a):
#         if a[i] in b:
#                 b.append(a[i])
#         else:
#                 b.append(a[i])
#         i+=1
# print(b)


# list=["21",22,1,"Megha","ankita"]
# i=0
# b=[]
# while i<len(list):
#         if type (list[i])!=(int):
#                 b.append(list[i])
#         i+=1
# print(b)



# l=[2,3,1,[2,3,[4,5],6]]
# i=0
# sum=0
# while i<len(l):
#         if type(l[i])==list:
#                 j=0
#                 while j<len(l[i]):
#                         sum+=l[i][j]             
#                         j+=1
#         else:
#                 sum+=l[i]
#         i+=1
# print(sum)



# a=[2,3,4,[5,6,7]]
# i=0
# sum=0
# while i<len(a):
#         if type(a[i])==list:
#                 j=0
#                 while j<len(a[i]):
#                         sum+=a[i][j]
#                         j+=1
#         else:
#                 sum+=a[i]
#         i+=1
# print(sum)
# a="saloni"
# b=5
# l=[]
# for i in range(len(a)):
#         l.append(a[i])
#         l.append(b*(i+1))
# print(l)


a="meghasharma"
if type(a)==str:
        a1=a[0].upper()+a[1:-1]+a[-1].upper()
        print(a1)