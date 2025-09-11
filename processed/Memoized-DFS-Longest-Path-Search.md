# 📚 Key Takeaways from Longest Path in a Grid


## 🧠 Core Concepts 💡

### Memoization: The Efficiency Boost 🚀

*   The `@functools.lru_cache(None)` decorator is crucial for performance.
*   **Without Memoization:** Exponential time complexity due to repeated calculations.  The algorithm would time out on larger grids.
*   **With Memoization:** Each subproblem (`i`, `j`, `turned`, `num`, `dir`) is solved only once. Subsequent calls are instant lookups.  This significantly reduces time complexity.

### The Main Loop: Kicking off the Search 🏁

*   The `return max((1 + dfs(...) for ... if num == 1 for ...), default=0)` statement drives the process:
    *   Iterates through each cell (`i`, `j`) in the grid.
    *   If a `1` is found, it initiates a DFS search from that cell in all four diagonal directions (`d`).
    *   Calculates the path length as `1` (starting cell) + the result of the recursive DFS call.
    *   `max(..., default=0)` selects the longest path and handles the case where no `1` exists (returning `0`).

## 📈 Complexity Analysis 📊

*   **Time Complexity:** O(n × m)
    *   Memoization ensures each state (`i`, `j`, `turned`, `num`, `dir`) is computed at most once.
    *   The total number of states is proportional to n × m.

*   **Space Complexity:** O(n × m)
    *   Space is primarily used by the memoization cache and the recursion stack, both proportional to the number of grid cells.


✅ **Action Items:**

*   Implement the solution using Python and the `@functools.lru_cache` decorator.
*   Test the solution on various grid sizes to verify performance improvements.
*   Consider alternative optimization techniques if further performance gains are needed for extremely large grids.
