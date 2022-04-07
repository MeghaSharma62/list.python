n=int(input("Enter the number"))
a=[1,2,3,9,14,20]
i=0
sum=0
while i<len(a):
        if a[i]<n:
                sum+=a[i]
        i+=1
print(sum)
                
