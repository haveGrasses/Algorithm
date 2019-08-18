import heapq


def get_least_numbers_big_data(alist, k):
    """ 不要看这个方法，那个if-else不好 """
    max_heap = []
    if not alist or k <= 0 or k > len(alist):
        return
    for ele in alist:
        ele = -ele
        if len(max_heap) < k:
            heapq.heappush(max_heap, ele)
        else:
            heapq.heappushpop(max_heap, ele)
    return list(map(lambda x: -x, max_heap))


def get_least_numbers_big_data2(alist, k):
    """ recommended """
    max_heap = []
    if not alist or k <= 0 or k > len(alist):
        return
    for i in alist:
        heapq.heappush(max_heap, -i)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return list(map(lambda x: -x, max_heap))


def get_greatest_numbers_big_data(alist, k):
    min_heap = []
    if not alist or k <= 0 or k > len(alist):
        return
    for i in alist:
        heapq.heappush(min_heap, i)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap


if __name__ == "__main__":
    l = [1, 9, 2, 4, 7, 6, 3]
    print(get_least_numbers_big_data(l, 3))
    print(get_greatest_numbers_big_data(l, 3))
    print(get_least_numbers_big_data2(l, 3))
