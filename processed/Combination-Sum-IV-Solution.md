# 📚 Key Takeaways from Combination Sum IV

> This document summarizes the problem statement, constraints, and a Python solution for the "Combination Sum IV" LeetCode problem.  The problem involves finding the number of distinct combinations of numbers from a given array that sum up to a target value.  A dynamic programming approach using depth-first search is presented for efficient solution.


## 🧠 Core Concepts 💡

### Problem Statement 🎯

*   Given an array of *distinct* integers `nums` and a target integer `target`.
*   Find the number of *possible combinations* that add up to `target`.
*   Different sequences are counted as different combinations.


### Constraints 🚧

*   `1 <= nums.length <= 200`
*   `1 <= nums[i] <= 1000`
*   All elements in `nums` are unique.
*   `1 <= target <= 1000`


### Examples ✨

*   **Example 1:** `nums = [1,2,3]`, `target = 4`. Output: `7`  (Combinations: (1,1,1,1), (1,1,2), (1,2,1), (1,3), (2,1,1), (2,2), (3,1))
*   **Example 2:** `nums = [9]`, `target = 3`. Output: `0` (No combinations possible)


## 💻 Python Solution using Dynamic Programming (DFS) 🐍

```python
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [1] + [-1] * target  # Initialize DP array. 1 for target=0, -1 for others

        def dfs(target: int) -> int:
            if target < 0:
                return 0
            if dp[target] != -1:
                return dp[target]  # Memoization: Use existing result

            dp[target] = sum(dfs(target - num) for num in nums)
            return dp[target]

        return dfs(target)
```

### Solution Explanation 📝

*   A `dp` array is used for *memoization* to store results of subproblems.
*   `dfs(target)` recursively explores all combinations.
*   Base case: `target < 0` returns 0 (invalid combination).
*   Memoization: If `dp[target]` is not -1, it returns the pre-computed result.
*   Recursive step:  sums the results of `dfs(target - num)` for each `num` in `nums`.


## ✅ Action Items

*   [ ]  Test the provided Python code with various inputs to verify correctness.
*   [ ]  Explore alternative approaches to solving this problem (e.g., iterative DP).
*   [ ]  Analyze the time and space complexity of the provided solution.


