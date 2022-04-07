# List product excluding duplicates.

List = [6,1,3,5,6,3,1]
# Output: 60
i=0
prod=1
b=[]
while i<len(List):
        if List[i]not in b:
                b.append(List[i])
                prod=prod*(b[i])
        i+=1
print(b,prod)
