# whether a num is prime or not

count=0
n=int(input("enter the num"))
i=1
while i<=n:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
    print(n,"prime num")
else:
    print(n,"not a prime")