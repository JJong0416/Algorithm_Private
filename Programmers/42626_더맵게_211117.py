import heapq

def solution(scoville, K):
    ans = 0
    hq = scoville
    heapq.heapify(hq)

    while len(hq) >= 2:
        if hq[0] >= K or len(hq) < 2:
            break

        min_hot = heapq.heappop(hq)
        min_next_hot = heapq.heappop(hq)
        heapq.heappush(hq, min_hot + min_next_hot * 2)
        ans += 1

    if hq[0] < K:
        return -1
    else:
        return ans