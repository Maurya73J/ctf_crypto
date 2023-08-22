file = open("rawoutputs.txt","r")
k=0
a=[]
b=[]
with open("rawoutputs.txt") as f:
    alist = [line.strip() for line in f]
for i in alist:
    if i=='':
        continue
    a.append(i)
for j in a:
    if k%2==1:
        b.append(j)
    k=k+1
print(b)

