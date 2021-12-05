import heapq


def solution(operations):
    heap = []
    max_heap = []

    for o in operations:
        cmd, num = o.split()
        num = int(num)

        if cmd == "I":
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (num * -1, num))
        else:
            if len(heap) == 0 or len(max_heap) == 0:
                pass
            elif num == 1:
                max_val = heapq.heappop(max_heap)[1]
                heap.remove(max_val)
            elif num == -1:
                min_val = heapq.heappop(heap)
                max_heap.remove((min_val * -1, min_val))

    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        return [0, 0]