# a=[1,2,6,3,4,5,7,8,9,7]
# i=0
# prod=1
# sum=0
# while i<len(a):
#         if i<=4:
#                 prod*=a[i]
#         else:
#                 sum+=a[i]
#         i+=1
# print(prod)
# print(sum)


def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)
    return a

result = outer_fun(5, 10)
print(result)