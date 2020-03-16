n=int(input("enter the value of n"))
if n>1:
    for i in range(2,n):
        if n%i==0 and n!=2:
            print("it is not a prime num",n)
            break
    else:
        print("it is a prime number",n)

