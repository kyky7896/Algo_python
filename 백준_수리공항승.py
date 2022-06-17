N,L=map(int,input().split())
coord=[False]*1001 #구멍이 1000개 나있음

for i in map(int,input().split()):
    coord[i]=True

ans=0 #테이프 몇개 썼는지 저장하는 변수
x=0 #x좌표
while x<1001:
    if coord[x]:
        ans+=1 #테이프 한개 씀 
        x+=L #x좌표 테이프 길이만큼 증가
    else:
        x+=1
print(ans)