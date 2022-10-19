N,K=map(int, input().split())
coins=[int(input()) for _ in range(N)]
coins.reverse() #리스트를 reverse해줌

ans=0
for coin in coins:
    ans+=K // coin #나누는 값이 너무 크면 0이라는걸 간과함 
    K %= coin #K를 coin으로 나누었을때 나머지값을 넣어줌 
print(ans)
    