# [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
# Join the said two lists element wise:
# [['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]


a=[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
b=[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
i=0
d=[]
while i<len(a):
        j=0
        while j<len(a[i]):
                e=a[i]+b[i]
                # d.append(e)
                j+=1
        d.append(e)
        i+=1
print(d)