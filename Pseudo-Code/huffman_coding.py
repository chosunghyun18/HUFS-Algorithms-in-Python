#%%
import heapq
from collections import defaultdict


def encode(frequency):
    heap = [{freq, str(freq)} for freq in frequency]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))




huff = encode([43, 13, 12, 16, 9 ,7])
print( "Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
for p in huff:
    print (p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])

# %%
