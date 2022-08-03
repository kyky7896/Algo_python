
stu_list=[]
for i in range(int(input())):
    [name, kor, eng, math]=map(str,input().split())

    stu_list.append([name, int(kor), int(eng), int(math)])
    #리스트의 각 원소가 튜플형태로 존재할 때, 우선순위에 맞게 원소를 정렬
stu_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in stu_list:
    print(student[0])