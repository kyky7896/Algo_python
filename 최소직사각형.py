# 한쪽을 짧은 부분, 한쪽을 긴 부분으로 몰아서 정렬한다
#[0] : 짧은부분 [1]:긴부분
def solution(sizes):
    num1 = 0
    num2 = 0
    answer=0
    change = 0
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
          change=sizes[i][0]
          sizes[i][0]=sizes[i][1]
          sizes[i][1]=change
        # sizes[i][0]을 돌면서 최댓값 구하기
        if num1 == 0 or sizes[i][0]>num1:
          num1=sizes[i][0]
        # sizes[i][1]을 각각 돌면서 최댓값 구하기
        if num2 ==0 or sizes[i][1]>num2:
          num2=sizes[i][1]
    answer=num1*num2
    return answer
