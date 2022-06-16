import math

N,K=map(int, input().split())
c_list=[int(input()) for _ in range(N)]

count=0
while(len(c_list)!=0): #0일때까지 while문 
    pop=c_list.pop(-1)
    lastMod=(K/pop)
    if(lastMod>=1):
        count+=math.floor(lastMod)
    K=K%pop
print(count)
