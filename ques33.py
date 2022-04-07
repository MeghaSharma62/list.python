# Write a Python program to sum two or more lists, the lengths of the lists may be different. 
# Original list:
# [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths:
# [4, 8, 8]


# n=[[1, 2, 4], [2, 4, 4], [1, 2,0]]
# i=0
# sum=0
# sum1=0
# sum2=0
# while i<len(n):
#         # if type (n[i])==list:
#                 # j=0
#                 # while j<len(n[i]):
#                 #         j=j+1
#                 sum=sum+(n[i][0])
#                 sum1=sum1+(n[i][1])
#                 sum2=sum2+(n[i][2])
#                 # j+=1
#                 i+=1
# print(sum,sum1,sum2)

  


n=[[3,4,5],[7,8,9],[1,2,6]]
i=0
b=[]
while i<len(n):
        b.append(n[i][0])
        i+=1
print(b)