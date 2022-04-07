# Remove empty List from List        
# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]

n=[5, 6, [], 3, [], [],"over", 9]
i=0
a=[]
while i<len(n):
        if n[i]!="over":
                a.append(n[i])
        i+=1
print(a) 
     
     