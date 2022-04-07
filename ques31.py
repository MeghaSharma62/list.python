# Write a Python program to join two given list of lists of same length, element wise. 
# Original lists:
# [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# Join the said two lists element wise:
# [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]





a=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
b=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
d=[]
while i<len(a):
        j=0
        while j<len(a[i]):
                c=a[i]+b[i]
                j+=1
        d.append(c)
        i+=1
print(d)

