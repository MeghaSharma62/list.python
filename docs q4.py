# Count unique values inside a list.


input_list = [1, 2, 2, 5, 8, 4, 4, 8]
i=0
b=[]
count=0
while i<len(input_list):
        if input_list[i] not in b:
                b.append(input_list[i])
                count+=1
        i+=1
print(b,count)

