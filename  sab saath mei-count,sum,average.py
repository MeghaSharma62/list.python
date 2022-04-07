# sab saath mei-count,sum,average


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
count=0
count1=0
a=[]
b=[]
while i<len(elements):
        if elements[i]%2==0:
                sum=sum+elements[i]
                count+=1
                a.append(elements[i])
        else:
                sum1=sum1+elements[i]
                count1+=1
                b.append(elements[i])
        i+=1
print(a,sum,count,"average",sum/count)
print(b,sum1,count1,"average1",sum1/count1)
