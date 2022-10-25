arr1=[[1,2],[2,3]]
arr2=[[3,4],[5,6]]
def solution(arr1, arr2):
    last_answer=[]
    for i in range(len(arr1)):
      ## 2중 list를 위해 생성
      answer = []
      for j in range(len(arr1[i])):
        answer.append(arr1[i][j]+arr2[i][j])
      last_answer.append(answer)
    return last_answer

solution(arr1,arr2)