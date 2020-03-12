import math

def solution(progresses, speeds):

    empty = [] #비어있는 리스트 생성 (여기에 소요되는 일자를 넣어줌)

    while progresses != [] and speeds != []:

        a = progresses.pop() #진행 %
        b = speeds.pop() #진행 속도
        c = math.ceil( (100 - a) / b ) #소요 일수

        empty.insert(0,c) #empty list에 소요일수를 넣어줌

    empty_dict = {} #각 소요일수를 키값으로 묶기 위한 딕트 생성

    for i in range(len(empty)):
        if i == 0:
            empty[i] = empty[i] #첫번째 element는 그대로 적용
            try:
                empty_dict[empty[i]] += 1 #딕트 값에 1 추가
            except:
                empty_dict[empty[i]] = 1

        elif empty[i] <= empty[i-1]: #두번째 element부터는 앞선 element보다 작을경우 앞 element 숫자를 따라감, 클 경우 그대로
            empty[i] = empty[i-1]
            try:
                empty_dict[empty[i]] += 1
            except:
                empty_dict[empty[i]] = 1
        else:
            empty[i] = empty[i]
            try:
                empty_dict[empty[i]] += 1
            except:
                empty_dict[empty[i]] = 1

    return list(empty_dict.values())

progresses = [93,30,55]
speeds = [1,30,5]

print(solution(progresses, speeds))

