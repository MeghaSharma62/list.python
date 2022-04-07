#  How to find all pairs in an array of integers whose sum is equal to the
# given number?




n = [10, 11, 12, 13, 14, 17, 18, 19]
number=30
list=[]
i=0
while i<len(n):
        j=0
        while j<len(n):
                a=n[i]
                m=n[j]
                if n[i]+n[j]==number:
                        list.append([a,m])
                j+=1
        i+=1
print(list)





# n=int(input("Enter the number"))
# i=1
# sum=0
# while i<100:
#         i=sum+1
#         sum=i*2
#         print(sum,end=" ")
#         i+=1
