n=int(input("Enter the number of elements"))
i=0
b=[]
sum=0
while i<n:
        num=int(input("Enter the elements"))
        b.append(num)
        sum+=b[i]
        i+=1
print(sum)
