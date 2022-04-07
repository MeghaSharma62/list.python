n=[2,0,3,8,9,0,4,0,5]
i=0
b=[]
c=[]
while i<len(n):
        if n[i]==0:
                b.append(n[i])
        else:
                c.append(n[i])
        i+=1
i=0
while i<len(b):
        c.append(b[i])
        i+=1
print(c)
