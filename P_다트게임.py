def solution(dartResult):
    answer = []
    dartResult=dartResult.replace("10", "A")
    sdt=['S','D','T']
    if dartResult[0]=='A':
      cnt=10
      #수로 시작
    else:
      cnt=int(dartResult[0])
    
    for i in dartResult[1:]:
      if i in sdt:
        cnt= cnt ** (sdt.index(i)+1)
      
      #문자 * 이면 현재수 두배, 이전수도 있으면 두배
      elif i=="*":
        cnt *=2
        if answer:
          answer[-1] *=2
      #문자가 '#'면 현재수 -
      elif i=='#':
        cnt=-cnt 
      #그외 문자면 숫자인것
      else:
        answer.append(cnt)

        if i=='A':
          i=10
        cnt=int(i)
    answer.append(cnt)
    return sum(answer)



dartResult='1S2D*3T'
solution(dartResult)
