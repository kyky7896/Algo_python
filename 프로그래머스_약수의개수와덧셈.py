left=13
right=17
def solution(left, right):
    answer = 0
    ##left의 약수 구하기
    for num1 in range(left,right+1):
        cnt=0
        for n in range(1, num1+1):
            if num1 % n == 0 :
                cnt+=1
                ## 짝수일때
        if cnt % 2 == 0:
            print("짝",num1)
            answer+=num1
            ## 홀수일때
        else:  
            print("홀",num1)
            answer-=num1
    print("answer",answer)
    return answer
solution(left,right)