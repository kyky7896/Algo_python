s="Zbcdefg"
def solution(s):
    answer=""
    lower_list=[]
    upper_list=[]
    for num in s:
        if (num.islower()):
            lower_list.append(ord(num))
        else :
            upper_list.append(ord(num))
    lower_list=sorted(lower_list, reverse=True)
    upper_list=sorted(upper_list, reverse=True)
    answer_list=lower_list+upper_list
    for ans in answer_list:
      answer+=(chr(ans))
    # print(answer)
    return answer
solution(s)

##다른 사람의 풀이
def solution1(s):
    return ''.join(sorted(s, reverse=True))