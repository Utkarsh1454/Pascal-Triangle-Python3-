rows = int(input("rows: "))

for index in range(0,rows):
    for spaces in range(rows,index,-1):
        print(' ', end='')#printing spaces
    number=1
    for col in range(0,index+1):
        print("%d " % number, end='')#space after %d
        number*=(index-col)/(col+1)#formula for pascal's triangle
    print()