# 📚 Key Takeaways from 1504. Count Submatrices With All Ones

> This document summarizes the problem of counting submatrices with all ones in a given binary matrix.  It details the problem statement, example inputs and outputs, and constraints, providing a clear understanding of the task and its complexities.

## 🧠 Core Concepts 💡

### Problem Statement 📝

* Given an *m x n* binary matrix `mat`, count the number of submatrices that contain only ones.

### Example Inputs and Outputs 📊

* **Example 1:**
    * Input: `mat = [[1,0,1],[1,1,0],[1,1,0]]`
    * Output: `13`  (Detailed breakdown provided in the original problem description)

* **Example 2:**
    * Input: `mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]`
    * Output: `24` (Detailed breakdown provided in the original problem description)


### Constraints ⚠️

* `1 <= m, n <= 150`
* `mat[i][j]` is either `0` or `1`.


## 🧮 Algorithm Considerations 🤔

This problem requires an efficient algorithm to avoid brute-force approaches, which would be computationally expensive for larger matrices.  A possible approach involves iterating through the matrix and, for each cell, calculating the number of submatrices it can be part of that contain only ones. This could involve dynamically tracking the size of contiguous blocks of ones.  Further analysis is needed to determine the optimal algorithm.

## ✅ Action Items 🎯

* Research and implement an efficient algorithm (e.g., dynamic programming) to solve the problem.
* Test the implemented algorithm thoroughly with various input matrices, including edge cases (e.g., all zeros, all ones).
* Analyze the time and space complexity of the chosen algorithm.  Aim for an optimal solution.

