# A는 5분, B는 1분, C는 10초
num=int(input())
a=b=c=0
if(num % 10 !=0):
    print(-1)
else:
    a=num//300
    num%=300
    # print(a,num)
    b=num//60
    num%=60
    # print(b,num)
    c=num//10
    num%=10
    # print(c,num)
    print(a, b, c)
