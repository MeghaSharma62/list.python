#  Write a program to print only odd numbers from the given list using  a while loop .





L = [23, 45, 32, 25, 46, 33, 71, 90]
i=0
b=[]
while i<len(L):
        if L[i]%2!=0:
                b.append(L[i])
        i+=1
print(b)