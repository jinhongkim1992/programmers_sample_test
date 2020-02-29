#위장
import numpy as np

def solution(clothes):

    #빈 딕셔너리 만들기
    dict_empty = {}
    #각 nested list는 옷과 카테고리의 조합이므로
    #해당 카테고리(key)에 있는 옷의 개수(value)를 dict로 만들어줌
    for nested_list in clothes:
            try:
                dict_empty[nested_list[1]] += 1
            except:
                dict_empty[nested_list[1]] = 1
    #각 dict의 value를 뽑은 리스트를 만들고,
    #해당 리스트 element에 모두 1을 더해준 조합을 만듬
    #해당 조합의 모든 case를 구하고 거기에 1을 빼줌
    #(빼준 1은 다 입지 않은 경우)
    the_list = list(dict_empty.values())
    the_list = [i + 1 for i in the_list]
    answer = np.prod(the_list) - 1

    return answer
