from typing import List
import heapq


class Solution:
    def getFinalState(
        self,
        nums: List[int],
        k: int,
        multiplier: int
    ) -> List[int]:

        MOD = 10**9 + 7
        n = len(nums)

        if multiplier == 1:
            return nums

        heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(heap)

        mx = max(nums)

        while k and heap[0][0] * multiplier <= mx:
            x, i = heapq.heappop(heap)

            x *= multiplier
            nums[i] = x

            heapq.heappush(heap, (x, i))
            k -= 1

        heap.sort()

        q, r = divmod(k, n)
        mul = pow(multiplier, q, MOD)

        for j, (x, i) in enumerate(heap):
            x = x % MOD
            x = x * mul % MOD

            if j < r:
                x = x * multiplier % MOD

            nums[i] = x

        return nums