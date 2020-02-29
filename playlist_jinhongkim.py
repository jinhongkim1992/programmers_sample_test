# 플레이리스트

import operator as op #특정 값 기준 정렬을 위한 operator import


def solution(genres, plays):
    index_list = []
    dict_all = {}

    for i in range(len(genres)):
        #각 장르(key)에 플레이수 sum(value)을 매칭하는 dict 생성
        try: dict_all[genres[i]] += plays[i]
        except: dict_all[genres[i]] = plays[i]

    #플레이수 기준으로 내림차순 정렬
    #베스트 장르순으로 플레이리스트 추출이 되어야 하기 때문에,
    #마지막 단계에서 활용
    sorted_genres = sorted(dict_all.items(), key = op.itemgetter(1),
                           reverse = True)

    #각 곡의 id값은 index 이기 때문에 index 리스트를 만들어 줌
    for i in range(len(genres)):
        index_list.append(i)
    #곡 id, 장르, 플레이수 튜플을 담고 있는 리스트를 생성
    set_all = list(zip(index_list, genres, plays))
    set_all.sort(key = op.itemgetter(2), reverse = True)

    #최종 리스트 만들기
    temp_list = []
    final_list = []

    for a in sorted_genres:
        for i in range(len(set_all)):
            #모든 튜플값에 대해서 가장 베스트 장르 순으로 베스트 곡 id 최대 두개 삽입
            if set_all[i][1] == a[0]:

                temp_list.append(set_all[i][0])
                if len(temp_list) == 2:
                    final_list.extend(temp_list)
                    temp_list = []
                    break

                elif genres.count(a[0]) == 1:
                    final_list.extend(temp_list)
                    temp_list = []
                    break

    return final_list
