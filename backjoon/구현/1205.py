'''1. 채점 중 20%에서 틀린 문제 -> 해결
sol 1: 조건을 최대한 세분화
sol 2: 랭킹리스트에 새로운 점수를 삽입하는 방식에서 count를 통해 구하는 방식으로 단순화'''
n, new_score, p = list(map(int, input().split()))

# n이 0보다 큰 경우에만 둘째 줄 입력 받아서 작업 수행
if n == 0:
    print(1)
else:
    cur_ranks = list(map(int, input().split()))
    # 현재 랭킹 리스트를 점수 기준으로 내림차순 정렬
    cur_ranks.sort(reverse=True)

    # 현재 랭킹 리스트에서 최소 점수 구하기
    min_score = cur_ranks[-1]

    rank = 0
    # 랭킹리스트 현재 개수와 랭킹리스트 최대 개수가 같은 경우
    if n == p:
        # 랭킹리스트 현재 최소 점수가 새로운 점수보다 크거나 같은 경우
        if min_score >= new_score:
            print(-1)
        else:
            # 기본 등수
            res = 1
            for i in range(n):
                # 랭킹 리스트 i번째 점수가 새로운 점수보다 큰 경우
                if cur_ranks[i] > new_score:
                    # 등수 증가
                    res += 1
            print(res)
    else:
        res = 1
        for i in range(n):
            if cur_ranks[i] > new_score:
                res += 1
        print(res)
