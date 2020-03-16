def factr(n):
    if n==1:
        return 1
    else:
        return n*factr(n-1)
print(factr(5))

