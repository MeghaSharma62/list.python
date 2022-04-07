# Remove duplicates from a list.
List = [1,2,3,1,2,2]
# Output: [1,2,3]


List = [1,2,3,1,2,2]
i=0
b=[]
while i<len(List):
        if List[i] not in b:
                b.append(List[i])
        i+=1
print(b)
