a=[2,1,6,5,7]
# b=[3,8,4,10,9]
i=0
c=[]
while i<len(a):
        c.append(a[i])
        # c.append(b[i])
        i+=1
print(c)
i=0
while i<len(c):
        j=0
        while j<len(c):
                if c[i]>c[j]:
                        m=c[i]
                        c[i]=c[j]
                        c[j]=m
                j=j+1
        i=i+1
print(c)                        
                        


# a=[1,5,6,4,8]
# i=0
# # b=[]
# while i<len(a):
#         j=0
#         while j<len(a):
#                 if a[i]<a[j]:
#                         c=a[i]
#                         a[i]=a[j]
#                         a[j]=c
                        
#                 j+=1
#         i+=1
# print(c)
                        