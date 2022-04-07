def new_func():
            n = [[5, 3, 7],
[1, 8, 9],
[6, 4, 2]
]    
    i=0
    row_sum=0
    while i<len(n):
            j=0
            while j<len(n):
                    row_sum=row_sum+n[i][j]
                    j+=1
            i+=1
            print(row_sum)

new_func()