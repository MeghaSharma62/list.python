# Write a Python program to concatenate element-wise three given lists. 
# Concatenate element-wise three said lists:
# ['0red100', '1green200', '2black300', '3blue400', '4white500']
# original lists:



a=['0', '1', '2', '3', '4'],
b=['red', 'green', 'black', 'blue', 'white'],
c=['100', '200', '300', '400', '500']
s=[]
i=0
while i<len(a):
     d=a[i]+b[i]+c[i]
     s.append(d)
     i+=1
print(s)

