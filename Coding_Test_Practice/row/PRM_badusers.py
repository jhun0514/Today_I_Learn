from itertools import permutations

def isMatchId(ban_id, user_id):
    for i in range(len(ban_id)):
        if ban_id[i] == '*': continue
        elif ban_id[i] != user_id[i]:
            return False
    return True

def check(banned_ids, candidate_users):
    for i in range(len(banned_ids)):
        if len(banned_ids[i]) != len(candidate_users[i]):
            return False
        if isMatchId(banned_ids[i], candidate_users[i]) is False:
            return False
    return True

def solution(user_ids, banned_ids):
    ans = list()

    for candidate_users in permutations(user_ids, len(banned_ids)):
        if check(banned_ids, candidate_users) is True:
            candidate_users = set(candidate_users)
            if candidate_users not in ans:
                ans.append(candidate_users)

    return len(ans)
