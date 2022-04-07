# Write a Python program to remove all the values except integer values from a given 
# array of mixed values. 
# Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']
# After removing all the values except integer values from the said array of mixed
# values: [12, 0]


a=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
b=[]
while i<len(a):
        if type(a[i])!=str and type(a[i])!=float:
                b.append(a[i])
        i+=1
print(b)



k=1
i=1
while i<=6:
      j=1
      while j<=i:
              if j%2==0:
                      print(0,end=" ") 
                      j=j+1
              k=k+1
      print() 
      i=i+1      


