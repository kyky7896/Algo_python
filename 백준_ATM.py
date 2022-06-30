n=int(input())
k=list(map(int, input().split()))
k.sort()

hap=0
s=0
#0,1,2,3,4
#0,1,2,3
#0,1,2
#0,1
#0
for i in range(len(k)): 
    for j in range(len(k)-s):
        hap+=(k[j])
    s+=1
print(hap)
