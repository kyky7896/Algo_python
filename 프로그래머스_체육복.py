n=5
l=[2,4]
re=[1,3,5]

f=[i for i in range(1,n+1)]
re=list(set(re)-set(l)) #순수하게 여벌 체육복 소지하고있는 학생수
lo=list(set(l)-set(re)) #순수하게 체육복을 잃어버린 학생
for r in re:
    if r-1 in lo: #re의 바로 앞의 수들이 lo안에 있으면
        lo.remove(r-1) #lo에서 제거 : 빌려준다는 뜻
    elif r+1 in lo: #여벌체육복 뒷번호 학생이 lo안에 있으면
        lo.remove(r+1)
print(n-len(lo))
