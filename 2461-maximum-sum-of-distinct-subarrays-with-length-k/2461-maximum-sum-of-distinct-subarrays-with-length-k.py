class Solution:
    def maximumSubarraySum(self, nums, k):
        freq_map = {}
        left = 0
        window_sum = 0
        max_sum = 0

        for right in range(len(nums)):

            # Add current element
            freq_map[nums[right]] = freq_map.get(nums[right], 0) + 1
            window_sum += nums[right]

            # Keep window size <= k
            if right - left + 1 > k:
                freq_map[nums[left]] -= 1
                window_sum -= nums[left]

                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]

                left += 1

            # Window has size k and all elements are distinct
            if right - left + 1 == k and len(freq_map) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum