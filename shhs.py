n = [[5, 3, 7],
[1, 8, 9],
[6, 4, 2]
]    
i=0
sum=0
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
while i<len(n):
        sum=sum+n[i][0]
        sum1=sum1+n[i][1]
        sum2=sum2+n[i][2]
        sum3=sum3+n[i][-2]
        sum4=sum4+n[i][-1]
        sum5=sum5+n[i][0]
        i+=1
        if sum==sum1==sum2==sum3==sum4==sum5:
                print("true")
        else:
                print("false this is not a magic square")
print(sum)
print(sum1)
print(sum2)
print(sum3)
print(sum4)
print(sum5)
