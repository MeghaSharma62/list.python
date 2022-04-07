# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# sum=0
# b=[]
# count=0
# while i<len(a):
#         if i==5:
#                 break
#         sum=sum+a[i]
#         # b.append(sum)
#         i+=1
# print(sum)

# sum and product of half-half list
a=[1,2,3,4,5,6,7,8,9,10]
i=0
sum=0
prod=1
while i<len(a):
        if i<=4:
                sum+=a[i]
        else:
                prod*=a[i]
        i+=1
print(sum)
print(prod)


# a=[1,2,3,4]
# b=[2,4,1,3]
# i=0
# d=[]
# while i<len(a):
#         c=a[i]+b[i]
#         d.append(c)
#         i+=1
# print(d)


