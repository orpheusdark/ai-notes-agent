# 📚 Key Takeaways from Integer Sum of Powers Problem


## 🧠 Core Concepts 💡

### Problem Definition 🤔
* Given two positive integers:
    * `n`: The target integer.
    * `x`: The exponent.
* Find the number of ways to express `n` as the sum of unique positive integers raised to the power of `x`.
    *  `n = n1<sup>x</sup> + n2<sup>x</sup> + ... + nk<sup>x</sup>` where `n1, n2, ..., nk` are unique positive integers.
* Return the result modulo `10<sup>9</sup> + 7` to handle large outputs.

### Example Cases 🧮
* **Example 1:**  `n = 10, x = 2`  Output: `1` (3² + 1² = 10)
* **Example 2:** `n = 4, x = 1` Output: `2` (4¹ = 4; 3¹ + 1¹ = 4)


## 💻 Solution Implementation 🐍

### Python Code  💻
```python
class Solution:
  def numberOfWays(self, n: int, x: int) -> int:
    MOD = 1_000_000_007
    # dp[i] := the number of ways to express i
    dp = [1] + [0] * n

    for a in range(1, n + 1):
      ax = a**x
      if ax > n:
        break
      for i in range(n, ax - 1, -1):
        dp[i] += dp[i - ax]
        dp[i] %= MOD

    return dp[n]
```

### Algorithm Explanation 💡
* **Dynamic Programming (DP):** The solution uses dynamic programming to efficiently count the number of ways.
* `dp[i]` stores the number of ways to express the integer `i` as a sum of unique integers raised to the power of `x`.
* The outer loop iterates through possible integers `a`.
* The inner loop updates `dp[i]` by adding the number of ways to express `i - a<sup>x</sup>` (since `a<sup>x</sup>` is added).
* The modulo operation (`%= MOD`) prevents integer overflow.


## ⚠️ Constraints 🚫

* `1 <= n <= 300`
* `1 <= x <= 5`


## ✅ Action Items 📝

* Analyze the time and space complexity of the provided dynamic programming solution.
* Explore alternative approaches to solve this problem, such as using recursion or other optimization techniques.
* Investigate the possibility of further improving the code's efficiency, especially for larger values of *n* and *x*.
