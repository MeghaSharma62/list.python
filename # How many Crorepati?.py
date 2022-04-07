# How many Crorepati?
# 1 - `Crorepati`
# 2 - `Lakhpati`
# 3 - `Dilwale`

# All those who have money more than or equal to 1 crore are known as Crorepati. All those who have money money greater than or equal
# to 1 lakh, those are called Lakhpati. Rest of the people are called Dilwale.

kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count=0
count1=0
count2=0
a=[]
b=[]
c=[]
while i<len(kitna_paisa_hai):
        if(kitna_paisa_hai[i])>10000000:
                a.append(kitna_paisa_hai[i])
                count+=1
        elif(kitna_paisa_hai[i])>100000:
                b.append(kitna_paisa_hai[i])
                count1+=1
        else:
                c.append(kitna_paisa_hai[i])
                count2+=1
        i+=1
print(a,count,"crorepati")
print(b,count1,"lakhpati")
print(c,count2,"dilwale")