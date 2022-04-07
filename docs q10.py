# count +ve and -ve

# Output: pos = 3, neg = 1

list2 = [-12, 14, 95, 3]
i=0
count=0
count1=0
a=[]
b=[]
while i<len(list2):
        if list2[i]>0:
                count+=1
                a.append(list2[i])
        else:
                count1+=1
                b.append(list2[i])
        i+=1
print(a,count)
print(b,count1)