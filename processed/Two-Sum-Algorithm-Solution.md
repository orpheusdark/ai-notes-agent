# 📚 Key Takeaways from Two Sum Algorithm 

> This document summarizes the "Two Sum" algorithm problem, its constraints, example inputs and outputs, and a provided C++ solution.  The core concept involves finding two numbers within an array that sum up to a specified target, returning their indices. The solution utilizes an `unordered_map` for efficient lookup.

## 🧠 Core Concepts 👨‍💻

### Problem Statement 🤔

* Given an array of integers (`nums`) and a target integer (`target`).
* Find two distinct numbers within the array that add up to the `target`.
* Return the *indices* of these two numbers.
* Assume exactly one solution exists.

### Constraints ⚠️

* `2 <= nums.length <= 104`  (Array length between 2 and 10,000)
* `-109 <= nums[i] <= 109` (Numbers in the array range from -10<sup>9</sup> to 10<sup>9</sup>)
* `-109 <= target <= 109` (Target value ranges from -10<sup>9</sup> to 10<sup>9</sup>)
* Only one valid answer exists.


### Example Inputs & Outputs 💡

* **Example 1:**
    * `nums = [2,7,11,15]`, `target = 9`
    * `Output: [0,1]` (because 2 + 7 = 9)

* **Example 2:**
    * `nums = [3,2,4]`, `target = 6`
    * `Output: [1,2]` (because 2 + 4 = 6)

* **Example 3:**
    * `nums = [3,3]`, `target = 6`
    * `Output: [0,1]` (because 3 + 3 = 6)


## 💻 C++ Solution Implementation 🚀

```cpp
class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> numToIndex;

    for (int i = 0; i < nums.size(); ++i) {
      if (const auto it = numToIndex.find(target - nums[i]);
          it != numToIndex.cend())
        return {it->second, i};
      numToIndex[nums[i]] = i;
    }

    throw;  //This will throw exception if no solution is found, but it's guaranteed to exist
  }
};
```

### Solution Explanation 📝

* An `unordered_map` called `numToIndex` is used to store each number from `nums` and its index.
* The code iterates through `nums`. For each number, it checks if `target - nums[i]` (the complement needed to reach the target) exists as a key in `numToIndex`.
* If found, the indices (value associated with the key and the current index `i`) are returned.
* If the complement is not found, the current number and its index are added to `numToIndex`.
* A `throw;` statement is included in case no solution is found (although the problem statement guarantees one exists).


## ✅ Action Items 🎯

*  Review the time and space complexity of the solution. *(O(n) time, O(n) space)*
* Explore alternative solutions (e.g., nested loops) and compare their efficiency.
* Consider edge cases and error handling (although guaranteed to have a solution).


