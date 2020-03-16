n=int(input("enter the value of n"))
for i in range(2,n):
    if n%2==0 and i!=2:
        print("it is not a prime num",n)
else:
    print("it is a prime number",n)

