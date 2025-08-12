# 📚 Key Takeaways from Integer Sum of Powers Problem

> This document summarizes the problem of expressing an integer *n* as a sum of unique integers raised to the power of *x*, detailing the solution approach and key constraints.  The Python solution utilizes dynamic programming for efficient calculation of the number of ways modulo 10<sup>9</sup> + 7.

## 🧠 Core Concepts 💡

### Problem Statement
* Given positive integers `n` and `x`, find the number of ways to express `n` as the sum of unique positive integers raised to the power of `x`.
*  `n = n1<sup>x</sup> + n2<sup>x</sup> + ... + nk<sup>x</sup>`, where `n1, n2, ..., nk` are unique positive integers.
* Return the result modulo 10<sup>9</sup> + 7.

### Example Cases
* **Example 1:** `n = 10, x = 2`. Output: 1 (3² + 1² = 10)
* **Example 2:** `n = 4, x = 1`. Output: 2 (4¹ = 4; 3¹ + 1¹ = 4)

### Constraints ⚠️
* 1 <= n <= 300
* 1 <= x <= 5


## 💻 Solution Approach 💻

* **Dynamic Programming:** A dynamic programming approach is used to efficiently calculate the number of ways.
* `dp[i]` represents the number of ways to express `i` as the sum of unique integers raised to the power of `x`.
* The algorithm iterates through possible integers `a`, calculating `a<sup>x</sup>`.
* For each `a<sup>x</sup>`, it updates `dp[i]` by adding `dp[i - a<sup>x</sup>]` for `i` values greater than or equal to `a<sup>x</sup>`.
* The modulo operator (`%`) ensures the result stays within the required range.


## 🐍 Python Code Implementation 🐍

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

## ✅ Action Items

* **Further Optimization:** Explore potential optimizations for larger values of `n` and `x`, as the current solution's time complexity might be improved.
* **Testing:** Conduct thorough testing with various input values to validate the correctness and efficiency of the implemented solution.
