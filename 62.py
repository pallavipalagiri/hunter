a=int(input())
b=list(map(int,input().split()))
p=[]
for i in range(a):
    for j in range(a):
        if(j>i):
            p.append(b[j]-b[i])
print(max(p))
