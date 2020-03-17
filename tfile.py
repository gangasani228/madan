with open("file.txt","r") as f:
    data=f.read()
    k=data.split("\n")
    print(k)
with open("file1.txt","r") as f1:
    data1=f1.read()
    k1= data1.split("\n")
    print(k1)
    f1.close()
for s in k:
    if s in k1:
        print(s)