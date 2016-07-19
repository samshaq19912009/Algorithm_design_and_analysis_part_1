import heapq
import sys

X = [int(l) for l in open(sys.argv[1])]

H_low = []
H_high = []
sum = 0

for xi in X:
    if len(H_low) > 0:
        if xi > -H_low[0]:
            heapq.heappush(H_high, xi)
        else:
            heapq.heappush(H_low, -xi)
    else:
        heapq.heappush(H_low, -xi)

    if len(H_low) > len(H_high) + 1:
        heapq.heappush(H_high, -(heapq.heappop(H_low)))
    elif len(H_high) > len(H_low):
        heapq.heappush(H_low, -(heapq.heappop(H_high)))

    sum += -H_low[0]

print sum % 10000
