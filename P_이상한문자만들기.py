s="tRy hello  WORLD"
def solution(s):
    answer = ''
    s=s.split(' ')
    for i in s:
      print("답뭐야",i,"끝")
      for j in range(len(i)):
        if j % 2 == 0:
          answer+=i[j].upper()
        else:
          answer+=i[j].lower()
      answer+=" "
      print("답",answer,"답")
    return answer
solution(s)