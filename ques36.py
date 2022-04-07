n=[[3,4,5],[7,8,9]]
i=0
b=[]
while i<len(n):
        if type(n[i])==list:
                j=0
                while j<len(n[i]):
                        b.append(n[i][j])
                        j+=1
        else:
                b.append(n[i])
                
        i+=1
print(b)
n=[[3,4,5],[7,8,9]]
i=0
b=[]
while i<len(n):
        if type(n[i])==list:
                j=0
                while j<len(n[i]):
                        b.append(n[i][j])
                        j+=1
        else:
                b.append(n[i])
                
        i+=1
print(b)
