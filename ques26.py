# sum of digits numbers in a list
# The original list is : [15, 81, 11, 234]
# List Integer Summation : [6,9,2,9]


n=[15,81,11,234]
i=0
b=[]
while i<len(n):
        a=str(n[i])
        j=0
        sum=0
        while j<len(a):
                sum=sum+int(a[j])
                j+=1
        b.append(sum)
        i+=1
print(b)

