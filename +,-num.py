# print the pattern
# 1,-2,3,-4,5,-6,7,-8,9,.....99,-100

i=1
while i<=100:
    if i%2==0:
        print(-i)
    else:
        print(+i)
    i=i+1