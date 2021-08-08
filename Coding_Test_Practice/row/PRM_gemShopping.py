# Brute Force
def solution(gems):
    TYPE_NUM = len(set(gems))
    GEM_NUM = len(gems)
    answer = []
    start, end = 0, 0
    DIST, INDEX = 0, 1

    cur_shop = {gems[0]: 1}
    while start < GEM_NUM and end < GEM_NUM:
        if len(cur_shop) < TYPE_NUM:
            end += 1
            if end == GEM_NUM:
                break
            cur_shop[gems[end]] = cur_shop.get(gems[end], 0) + 1
        else:
            answer.append((end-start, [start+1, end+1]))
            cur_shop[gems[start]] -= 1
            if cur_shop[gems[start]] == 0:
                del cur_shop[gems[start]]
            start += 1
    answer = sorted(answer, key=lambda x: (x[DIST], x[INDEX]))
    return answer[0][INDEX]
