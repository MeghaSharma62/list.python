# Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

n=[12,67,98,34]
i=0
sum=0
b=[]
while i<len(n):
        if type (n[i])==list:
                j=0
                while j<len(n[i]):
                        sum+=n[i]
                        b.append(sum)
                j+=1
        i+=1
print(b)
n=[12,67,98,34]
i=0
# sum=0
b=[]
while i<len(n):
        a=str(n[i])
        j=0
        sum=0
        while j<len(a):
                sum=sum+int(a[j])
                # b.append(sum)
                j=j+1
        b.append(sum)
        i=i+1
print(b) 


