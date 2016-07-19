#Using bisect: 3.26s
#Using my own binary_search 9.74s


import bisect
from time import time
import sys


def binary_search(nums, target, bigger):
    n = len(nums)
    l, r = 0, n-1
    while l <= r:
        mid = (l+r) / 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            if bigger:
                l = mid + 1
            else:
                r = mid - 1

    return l


def two_sum(array):
    WIDTH = 10000
    out = set()
    for i in array:
        #lower = binary_search(array, -WIDTH-i, False)
        #upper = binary_search(array, WIDTH-i, True)
        lower = bisect.bisect_left(array, -WIDTH-i)
        upper = bisect.bisect_right(array, WIDTH-i)
        out |= set([i+j for j in array[lower:upper]])
    return out

def main():
    array = []
#    file = sys.argv[1]
    with open('2sum.txt') as file_in:
        for line in file_in:
            num = int(line.strip())
            array.append(num)
    array.sort()
    return len(two_sum(array))

if __name__ == '__main__':
    start = time()
    print main()
    print time() - start
