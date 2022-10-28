def solution(s):
    dict={"zero":0, "one":1,"two":2,"three":3, "four":4,
    "five":5, "six":6, "seven":7,
    "eight":8, "nine":9}
    
    answer=''
    words=''
    for j in range(len(s)): ## 영단어를 하나씩 for문 돌린다
      if s[j].isdigit(): ##숫자면
        answer+=s[j]
      else: ##숫자가 아닐때
        words+=s[j]
        for i in dict.keys():
          if i == words :
            answer+=str(dict[i])
            words=''
    return answer


solution("one4seveneight")