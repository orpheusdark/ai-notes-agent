# 🧮 24 Game Solver: Key Takeaways

> This document summarizes the rules and constraints of the 24 Game, a mathematical puzzle involving four cards and the goal of creating an expression that evaluates to 24 using basic arithmetic operations.  The document highlights the key constraints, including real division, binary operations, and the prohibition against concatenation.


## 🧠 Core Concepts 💡

### Problem Statement 🤔

The goal is to determine if it's possible to arrange four cards (numbers 1-9) using +, -, *, /, and parentheses to obtain a result of 24.

*   **Input:** An integer array `cards` of length 4, where each element represents a card with a number between 1 and 9.
*   **Output:** `true` if a valid expression resulting in 24 exists; `false` otherwise.

### Constraints 🚧

*   **Real Division:** `/` represents real-number division (e.g., 4 / (1 - 2/3) = 12).
*   **Binary Operations:** Operators are applied between exactly two numbers; unary minus is not allowed.
*   **No Concatenation:** Numbers cannot be concatenated (e.g.,  `1` and `2` cannot form `12`).


## 🧮 Allowed Operations ➕➖✖️➗

*   Addition (`+`)
*   Subtraction (`-`)
*   Multiplication (`*`)
*   Division (`/`)
*   Parentheses (`(` and `)`) to control order of operations.


## ⚠️ Prohibited Operations 🚫

*   Unary minus (e.g., `-1 + 2 + 3`)
*   Number concatenation (e.g., creating `12` from `1` and `2`)

## 🧪 Example Cases 🧪

*   **Example 1:** `cards = [4, 1, 8, 7]`  ➡️ Output: `true`  (`(8 - 4) * (7 - 1) = 24`)
*   **Example 2:** `cards = [1, 2, 1, 2]`  ➡️ Output: `false` (No valid expression sums to 24)


## ✅ Action Items

*   Develop an algorithm to efficiently check all possible combinations of operations and parentheses to determine if a solution exists.  Consider backtracking or dynamic programming approaches.
*   Implement the algorithm in a chosen programming language (e.g., Python, Java, C++).
*   Write unit tests to verify the correctness of the algorithm for various input cases, including edge cases and examples provided.
