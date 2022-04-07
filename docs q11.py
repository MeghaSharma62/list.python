# input: start = -4, end = 5
# Output: -4, -3, -2, -1


start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for num in range(start, end + 1):
    if num < 0:
        print(num, end = " ")