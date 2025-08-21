
# **📊 1504. Count Submatrices With All Ones**


## **🎯 Problem Overview**

Given an `m x n` binary matrix `mat`, where each cell is either `0` or `1`, your task is to count the number of **submatrices** (rectangles of all sizes) that consist entirely of `1`s.

👉 This problem is a **generalization of counting squares** ➡️ to **counting all rectangles**, making it more challenging but also more interesting! ✨

---

## **✨ Examples to Clarify**

### **Example 1:**

```
Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
```

**Explanation:**

* ✅ 6 rectangles of size **1x1** 🟦
* ✅ 2 rectangles of size **1x2** ➡️
* ✅ 3 rectangles of size **2x1** ⬇️
* ✅ 1 rectangle of size **2x2** 🔲
* ✅ 1 rectangle of size **3x1** 🔻
* **Total:** `6 + 2 + 3 + 1 + 1 = 13` 🎉

---

### **Example 2:**

```
Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
```

**Explanation:**

* ✅ 8 rectangles of **1x1**
* ✅ 5 rectangles of **1x2**
* ✅ 2 rectangles of **1x3**
* ✅ 4 rectangles of **2x1**
* ✅ 2 rectangles of **2x2**
* ✅ 2 rectangles of **3x1**
* ✅ 1 rectangle of **3x2**
* **Total:** `8 + 5 + 2 + 4 + 2 + 2 + 1 = 24` 🎯

---

## **🧠 Approach and Logic Building**

### **🚀 Brute Force vs. Efficient Solution**

* **Brute Force:**
  Check every possible top-left & bottom-right corner of a submatrix → **O(m²n²)** ⏳ (too slow for 150x150, i.e., `150⁴ = 50M+ operations`).
* **Efficient:**
  Use **dynamic programming + row compression** → reduces to **O(m²n)** ⚡.

---

### **🔑 Key Insight**

1. **Fix a top row** (`baseRow`) and consider all possible bottom rows.
2. **Compress columns** using bitwise AND → column = `1` only if all rows in that column (between baseRow & current row) are `1`.
3. For each compressed row, **count consecutive ones** → number of rectangles ending at each column.

📌 Complexity reduced to **O(m²n)** ✅

---

### **📝 Step-by-Step Logic**

1. **Initialize** `ans = 0`
2. For each `baseRow` in range `[0, m-1]`:

   * Set `row = [1] * n`
   * For each `i` from `baseRow → m-1`:

     * Update each `row[j] &= mat[i][j]`
     * Call helper `_count(row)` to count rectangles.
3. **Helper `_count(row)`**:

   * Maintain `length = 0`
   * For each `num` in row:

     * If `1` → extend sequence (`length+1`)
     * If `0` → reset (`length=0`)
   * Add `length` to result at each step.

---

### **🔍 Example Walkthrough (Example 1)**

* `baseRow = 0`: total = **4**
* `baseRow = 1`: total = **6**
* `baseRow = 2`: total = **3**
  👉 **Overall Total = 13 ✅**

---

## **💻 Code Explanation**

```python
class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m = len(mat)  # Number of rows
        n = len(mat[0])  # Number of columns
        ans = 0  # Initialize answer

        for baseRow in range(m):  # Consider each starting row
            row = [1] * n  # Temporary array for compressed columns
            for i in range(baseRow, m):  # For each ending row
                for j in range(n):  # Update each column
                    row[j] &= mat[i][j]  # AND with current row
                ans += self._count(row)  # Count rectangles for this compressed row
        return ans

    def _count(self, row: list[int]) -> int:
        res = 0  # Result for this compressed row
        length = 0  # Length of consecutive ones
        for num in row:
            length = 0 if num == 0 else length + 1  # Reset or extend
            res += length  # Add number of rectangles ending here
        return res
```

---

## **🧩 Code Breakdown**

* **`numSubmat`:**

  * Iterates through all possible top & bottom rows.
  * Compresses columns with AND operation.
  * Uses `_count` to compute rectangles.

* **`_count`:**

  * Counts consecutive ones → rectangles ending at each column.

---

## **⚡ Complexity Analysis**

* **Time:** `O(m²n)` ⏱️
* **Space:** `O(n)` 🗂️

---

## **🎉 Conclusion**

This problem efficiently counts all rectangle submatrices of ones by leveraging **row compression** and **dynamic programming**.

**🚀 Key Takeaways:**

* ✅ Use **row compression** for vertical continuity.
* ✅ Count **horizontal rectangles** in linear time.
* ✅ Avoid brute-force by **smart DP approach**.
