
# **🔢 [1277] Count Square Submatrices with All Ones**

## **📜 1. Problem Introduction & Understanding**

Imagine you're given a grid (like a digital image made of black 🖤 (`0`) and white 🤍 (`1`) pixels). Your task is to count **every single white square** that can be found in this image. Not just the big ones, but all possible squares of all sizes—from 1x1 pixels up to the largest possible.

A **submatrix** is any contiguous block within the larger grid. A **square submatrix** has equal height and width.

**The Challenge:** Find an efficient way to count *all* such squares without checking every possible square manually, which would be computationally expensive.

---

## **🎯 2. The Problem's Significance & Real-World Applications**

Why is this problem important?

*   **Computer Vision & Image Processing:** 🖼️ Counting squares or finding the largest solid block of pixels is fundamental in object detection, pattern recognition, and image segmentation.
*   **Data Analysis:** 📊 Analyzing datasets represented as matrices (e.g., user engagement grids, genetic data) often involves finding dense blocks of "1"s.
*   **Algorithmic Foundation:** 🧠 This problem is a classic application of **Dynamic Programming** and a slight variation of the famous "Maximal Square" problem. It's a common interview question that tests your ability to optimize a solution using DP.

---

## **🤔 3. Initial Approach: The Brute Force Idea (And Why It's Bad)**

The most straightforward way is to check every possible square.

1.  For every cell `(i, j)` that is a `1`, it's a 1x1 square. ✅
2.  For every possible top-left corner `(i, j)` and for every possible size `s` (from 2 up to the minimum of the grid's remaining rows and columns), check if the square of size `s` starting at `(i, j)` is filled with all `1`s.

**How to check a square of size `s`?** You would need to check `s x s` cells for each potential square. This leads to a time complexity of **O(m * n * min(m, n)³)**, which is far too slow for the given constraints (a 300x300 grid has 90,000 cells, and this approach could run billions of operations).

**We need a smarter, more efficient strategy.**

---

## **✨ 4. The "Aha!" Moment: Dynamic Programming**

The key insight is that a larger square is built from smaller ones. We can use a **Dynamic Programming (DP)** table to store answers to subproblems and build the solution bottom-up.

**DP Definition:**
Let `dp[i][j]` represent the **side length of the largest square** that has its **bottom-right corner** at the cell `(i, j)`.

But here's the magic: the value `dp[i][j]` also tells us **exactly how many squares** end at `(i, j)`. If the largest square ending at `(i, j)` has a side length of `3`, it means there are three squares ending there: a 1x1, a 2x2, and a 3x3.

**How do we compute `dp[i][j]`?**
It depends on the three adjacent cells: left `(i, j-1)`, top `(i-1, j)`, and top-left `(i-1, j-1)`.
*   If `matrix[i][j] == 0`, then `dp[i][j] = 0`. No square can end here.
*   If `matrix[i][j] == 1`, it can form a square. The size of this square is limited by the smallest square among its three neighbors. We take the minimum and add 1.

`dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`

**Why the minimum?** 🧐
To form a perfect square of size `k` at `(i, j)`, you must simultaneously form squares of *at least* size `k-1` at `(i-1, j)`, `(i, j-1)`, and `(i-1, j-1)`. Taking the minimum of these three ensures this condition is met. The `+1` accounts for the current cell.

| Visual Aid for the DP Relation |
| :--- |
| Imagine building a bigger square. The current cell `(i, j)` can only extend the square as far as its neighbors allow. If one neighbor only supports a 2x2 square, you cannot form a 3x3 square no matter how large the other neighbors are. |
| `?` `?` `?` |
| `?` `2` `2` |
| `?` `2` `?` → The `?` can only become `2 + 1 = 3` if all `?` are at least `2`. If one is only `1`, the `?` becomes `1 + 1 = 2`. |

---

## **🧮 5. Step-by-Step Example Walkthrough**

Let's use the example from the problem:
```
matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
```
We'll create our `dp` table. We can do this **in-place** (overwriting the original matrix to save space) or create a new table. The solution uses in-place modification.

**Initial `dp` / `matrix` state:**
```
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
```

**Process each cell (row-wise):**

1.  **Row 0:** Cells can only be 1x1 squares. `dp[0][j]` remains `matrix[0][j]`.
    *   `[0, 1, 1, 1]` -> `[0, 1, 1, 1]`

2.  **Row 1, Column 0:** `matrix[1][0] = 1`. It has no top-left or left neighbor (j=0). So it remains a 1x1 square.
    *   `[1, ?, ?, ?]` -> `[1, ?, ?, ?]`

3.  **Row 1, Column 1:** `matrix[1][1] = 1`.
    *   Check neighbors: `left=1`, `top=1`, `top-left=0`.
    *   `min(1, 1, 0) + 1 = 0 + 1 = 1`. ❌ Wait, this seems wrong. Let's think.
    *   Actually, the neighbors are `(i, j-1) = 1`, `(i-1, j) = 1`, `(i-1, j-1)=0`. The correct min is `0`.
    *   This means the largest square ending at `(1,1)` is only 1x1. So `dp[1][1] = 1`. But visually, we see a 2x2 square from `(0,0)` to `(1,1)` is not possible because `(0,0)` is `0`. So the calculation is correct.
    *   `[1, 1, ?, ?]`

4.  **Row 1, Column 2:** `matrix[1][2] = 1`.
    *   Neighbors: `left=dp[1][1]=1`, `top=dp[0][2]=1`, `top-left=dp[0][1]=1`.
    *   `min(1, 1, 1) + 1 = 1 + 1 = 2`.
    *   This means a 2x2 square ends here `(0,1)` to `(1,2)`. It also means a 1x1 square ends here.
    *   `[1, 1, 2, ?]`

5.  **Row 1, Column 3:** `matrix[1][3] = 1`.
    *   Neighbors: `left=2`, `top=1`, `top-left=1`.
    *   `min(2, 1, 1) + 1 = 1 + 1 = 2`.
    *   `[1, 1, 2, 2]`

6.  **Row 2, Column 0:** `matrix[2][0] = 0`. So `dp[2][0] = 0`.
    *   `[0, ?, ?, ?]`

7.  **Row 2, Column 1:** `matrix[2][1] = 1`.
    *   Neighbors: `left=dp[2][0]=0`, `top=dp[1][1]=1`, `top-left=dp[1][0]=1`.
    *   `min(0, 1, 1) + 1 = 0 + 1 = 1`.
    *   `[0, 1, ?, ?]`

8.  **Row 2, Column 2:** `matrix[2][2] = 1`.
    *   Neighbors: `left=1`, `top=2`, `top-left=1`.
    *   `min(1, 2, 1) + 1 = 1 + 1 = 2`.
    *   `[0, 1, 2, ?]`

9.  **Row 2, Column 3:** `matrix[2][3] = 1`.
    *   Neighbors: `left=2`, `top=2`, `top-left=2`.
    *   `min(2, 2, 2) + 1 = 2 + 1 = 3`.
    *   `[0, 1, 2, 3]`

**Final `dp` / `matrix` state:**
```
[
  [0, 1, 1, 1],
  [1, 1, 2, 2],
  [0, 1, 2, 3]
]
```
Now, the answer is the **sum of all values** in this DP table.
`0 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 0 + 1 + 2 + 3 = 15` ✅

This matches the expected output. Each value `dp[i][j] = k` contributes `k` squares to the total count.

---

## **💻 6. Code Explanation**

The provided solution is elegant and efficient. Let's break it down line by line.

```python
class Solution:
  def countSquares(self, matrix: list[list[int]]) -> int:
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == 1 and i > 0 and j > 0:
          matrix[i][j] += min(matrix[i - 1][j - 1],
                              matrix[i - 1][j], matrix[i][j - 1])
    return sum(map(sum, matrix))
```

# **Count Square Submatrices with All Ones**

This program counts all square submatrices filled with 1's in a binary matrix using dynamic programming.

**Key Logic:**
- For each cell `(i, j)` that contains a 1 (and isn't in the first row/column)
- Its value becomes: `1 + min(top, left, top-left neighbors)`
- This value represents how many squares end at this position
- The final answer is the sum of all values in the matrix

**Example:**
If a cell's value becomes 3, it means there are 3 squares ending here:
- 1×1 square
- 2×2 square  
- 3×3 square

**Time Complexity:** O(m×n)  
**Space Complexity:** O(1) (modifies input in-place)

The solution efficiently transforms a complex counting problem into a simple matrix traversal with minimal operations.
---

## **📊 7. Complexity Analysis**

| Complexity Type | Analysis |
| :--- | :--- |
| **Time Complexity** | **O(m * n)**. The algorithm simply iterates through each of the `m * n` cells in the matrix once and performs a constant-time operation (a min of three numbers and an addition) on each. |
| **Space Complexity** | **O(1)**. The solution uses the input matrix itself for DP storage, requiring no additional space proportional to the input size. (Note: If we weren't allowed to modify the input, the space complexity would be **O(m * n)** to create a separate DP table). |

---

## **✅ 8. Summary**

*   **Problem:** Count all square submatrices filled with `1`s in a binary grid.
*   **Brute Force:** Inefficient, with very high time complexity.
*   **Optimal Solution:** Dynamic Programming.
*   **DP Insight:** `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1` for `matrix[i][j] == 1`.
*   **Result:** The value `dp[i][j]` gives the number of squares that **end at** `(i, j)`. The answer is the sum of all `dp[i][j]`.
*   **Efficiency:** Linear time and constant space (if modifying input).

---

## **❓ 9. Viva Questions**

**Q1: What is the main idea behind the dynamic programming solution?**
*   **A:** The idea is that the size of the largest square ending at a cell `(i, j)` is determined by the smallest square among its three adjacent cells (left, top, top-left). This value also directly tells us how many squares end at that cell.

**Q2: Why do we take the minimum of the three neighboring values?**
*   **A:** To form a perfect larger square, all three possible smaller squares that form its foundation must be present. The smallest one dictates the limiting factor. If one neighbor only supports a 1x1 square, you cannot build a 2x2 square on top of it.

**Q3: What is the time and space complexity of the solution?**
*   **A:** The time complexity is **O(m * n)** where `m` is the number of rows and `n` is the number of columns. The space complexity is **O(1)** if we modify the input array, otherwise it's **O(m * n)** for a separate DP table.

**Q4: How would you handle the problem if you were not allowed to modify the input array?**
*   **A:** I would create a new 2D DP array of the same dimensions as the input. I would initialize it with zeros. Then, I would iterate through the input matrix. For the first row and first column, I would directly copy the values from the input (`dp[i][j] = matrix[i][j]`). For other cells, I would use the same DP formula: `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1` if `matrix[i][j] == 1`, else `0`. Finally, I would return the sum of all elements in the DP table.

**Q5: How is this problem related to the "Maximal Square" problem?**
*   **A:** The "Maximal Square" problem asks for the area of the *largest* square submatrix of all `1`s. The solution is nearly identical: you use the same DP recurrence relation to fill a table, but instead of summing all values at the end, you simply track the *maximum* value found in the entire DP table. The area of the largest square would then be `max_value * max_value`.
