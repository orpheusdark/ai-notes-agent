# 🎯 **Two Sum Problem: From Brute Force to Optimal Solution**

---

## 🥜 **The Problem in a Nutshell**

Imagine you're at a grocery store 🛒. You have a list of item prices and a specific total amount (`target`) you want to spend.
Your goal is to find **exactly two different items** in your cart whose prices add up to that total.

👉 The **Two Sum Problem** is exactly this, but instead of items, we have **numbers in an array**, and instead of prices, we return their **indices**.

---

## 🔍 **Deep Dive into the Problem Statement**

* **Input:**

  1. An array of integers `nums`. Example: `[10, 15, 3, 7]`
  2. A single integer `target`. Example: `17`

* **Goal:** Find two **distinct indices** `i` and `j` such that:

  > `nums[i] + nums[j] = target`

* **Output:** Return these indices. Example: `[0, 3]` (because `10 + 7 = 17`).

* **Important Guarantee:** Exactly **one valid solution** exists → no need to handle multiple/no answers. ✅

---

## ⚖️ **Constraints & Why They Matter** ⚠️

1. **`2 <= nums.length <= 10^4`**
   The array can be small or large. Brute force **O(n²)** won’t scale for `n = 10,000`. ⏳

2. **`-10^9 <= nums[i] <= 10^9`**
   Numbers can be huge, positive or negative ➕➖. Must handle carefully.

3. **`-10^9 <= target <= 10^9`**
   Target can also be very large.

4. **Only one solution exists** 🎯
   Stop as soon as you find the pair.

---

## 💡 **Examples to Solidify Understanding**

| Example | Input (nums)     | Target 🎯 | Explanation        | Output 📝 |
| :-----: | :--------------- | :-------: | :----------------- | :-------- |
|  **1**  | `[2, 7, 11, 15]` |    `9`    | `2 + 7 = 9`        | `[0, 1]`  |
|  **2**  | `[3, 2, 4]`      |    `6`    | `2 + 4 = 6`        | `[1, 2]`  |
|  **3**  | `[3, 3]`         |    `6`    | Must use both `3`s | `[0, 1]`  |
|  **4**  | `[1, -2, 5, 8]`  |    `3`    | `-2 + 5 = 3`       | `[1, 2]`  |
|  **5**  | `[10, 15, 3, 7]` |    `17`   | `10 + 7 = 17`      | `[0, 3]`  |

---

## 🧠 **Logic Building: The Thought Process**

### 1️⃣ Brute Force Approach 🤯

* Try **every possible pair** (nested loops).
* Works but is **O(n²)** → too slow for big inputs. ❌

---

### 2️⃣ Optimal Approach: Hash Map 💡

**Key Idea:** For each number `nums[i]`, look for its **complement**:
`complement = target - nums[i]`

* If complement already exists in our map → ✅ Solution found.
* If not, store current number with its index.

👉 Average lookup time in a hash map is **O(1)** ⚡

**Step-by-Step Example (`nums = [3, 2, 4], target = 6`)**

| Step | nums\[i] | Needed Number | Seen Map Before | Action                   | Seen Map After |
| ---- | -------- | ------------- | --------------- | ------------------------ | -------------- |
| 0    | 3        | 3             | `{}`            | Store `3:0`              | `{3:0}`        |
| 1    | 2        | 4             | `{3:0}`         | Store `2:1`              | `{3:0, 2:1}`   |
| 2    | 4        | 2             | `{3:0, 2:1}`    | ✅ Found! Return `[1, 2]` | -              |

---

## 💻 **Solution Implementations**

### 🖥️ C++ Solution

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Create a map to store number -> index
        unordered_map<int, int> numToIndex;

        for (int i = 0; i < nums.size(); ++i) {
            // Calculate the number we need to find
            int complement = target - nums[i];
            
            // Check if the complement exists in the map already
            if (numToIndex.find(complement) != numToIndex.end()) {
                // Found it! Return the stored index and the current index.
                return {numToIndex[complement], i};
            }
            // If not found, add the current number and its index to the map
            numToIndex[nums[i]] = i;
        }
        // The problem guarantees a solution, so this should never be reached.
        // It's here for code safety.
        return {}; // Return an empty vector (better practice than 'throw')
    }
};
```

---

### 🐍 Python Solution

```python
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}  # dictionary to hold number: index
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return []  # Fallback return
```

---

## ⏱️ **Time & Space Complexity**

* **Time:** O(n) → One pass, hash lookups are O(1) ⚡
* **Space:** O(n) → Need to store seen numbers 💾

---

## ✅ **Conclusion & Key Takeaways**

1. 🗝️ **Complement is Key:** Reframe `a + b = target` → `find target - a`.
2. ⚡ **Hash Maps = Speed:** Turns O(n²) brute force → O(n) optimal.
3. 🔄 **One-Pass Efficiency:** Build the map while traversing.
4. 🧩 **Pattern Recognition:** Two Sum is a template for harder problems.

**Now go solve it yourself! 🚀 Happy Coding!** 👨‍💻👩‍💻😊
