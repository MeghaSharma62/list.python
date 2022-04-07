a=[1,2,3,4,5]
i=0
coun=0
b=[]
while i<len(a):
        b.append(a[i])
        if coun==2:
                b.append(6)
        coun+=1
                # b.append(a[i])
        i+=1
print(b) 


