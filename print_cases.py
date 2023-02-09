depth = int(input("Enter memory depth > "))

numcases = 4**depth
lencases = len(bin(numcases-1)[2:])
# encodinglength = 0
# for i in range(depth+1):
#     encodinglength+=4**i
# print(f'encoding length => {encodinglength}\nnum cases => {numcases}')

for i in range(numcases):
    print('0'*(lencases-len(bin(i)[2:]))+bin(i)[2:])
