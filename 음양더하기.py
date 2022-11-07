def solution(absolutes, signs):
    answer=[]
    for i in range(len(absolutes)):
      if signs[i] == True:
        answer.append(absolutes[i])
      else:
        answer.append(absolutes[i]*-1)
    print(sum(answer))
    return answer

absolutes=[4,7,12]
signs=[True,False,True]
solution(absolutes, signs)