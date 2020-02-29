def solution(heights):
    answer = []

    while heights != []:
        a = heights.pop() #a라는 변수에 리스트 마지막 element 추가

        for i in range(1,len(heights)+1):
            #pop된 height 리스트에서 마지막 변수부터 비교함
            index_num = len(heights) - i
            #정답은 인덱스 값으로 넣어줘야하므로 index_num 변수 설정
            if heights[-i] > a:
                answer.insert(0,index_num+1)
                break
            elif i == len(heights):
                answer.insert(0,0)
            #더 높은 탑이 있으면 해당 인덱스 번호를 answer에 넣고, break
            #그렇지 않으면 0


    answer.insert(0,0)

    return answer
