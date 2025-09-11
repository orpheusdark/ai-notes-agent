# 📚 Key Takeaways from "Number of Zero-Filled Subarrays" Problem

> This document summarizes the problem of counting zero-filled subarrays within a given integer array.  It details the problem statement, examples, constraints, and potential approaches to solving it.  The key is to efficiently identify and count all contiguous subarrays composed solely of zeros.

## 🧠 Core Concepts 💡

### Problem Statement 🎯

Given an integer array `nums`, determine the total number of subarrays containing only zeros. A *subarray* is a contiguous, non-empty sequence within the array.

### Examples 🤔

* **Example 1:** `nums = [1,3,0,0,2,0,0,4]`  Output: 6 (Four [0]'s, two [0,0]'s)
* **Example 2:** `nums = [0,0,0,2,0,0]` Output: 9 (Three [0,0]'s, one [0,0,0], five single [0]'s)
* **Example 3:** `nums = [2,10,2019]` Output: 0 (No zero-filled subarrays)


### Constraints ⚠️

* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`


## 🧮 Solution Approach 🧮

A naive approach would involve iterating through all possible subarrays and checking if each contains only zeros. However, this has a time complexity of O(n^2), which is inefficient for larger input arrays.

A more efficient approach involves using a *sliding window* or a *pointer* technique to iterate through the array.  When a zero is encountered, a counter keeps track of the length of the zero-filled subarray.  The number of possible subarrays from this length is added to the total count. For example if a subarray of three zeros is found ([0,0,0]) there are 3 subarrays of this. [0], [0,0], [0,0,0].


## 🛠️  Pseudocode  💻

```python
count = 0
current_length = 0
for num in nums:
  if num == 0:
    current_length += 1
  else:
    count += current_length * (current_length + 1) // 2 # Sum of integers from 1 to current_length
    current_length = 0
count += current_length * (current_length + 1) // 2 # Handle trailing zeros
return count
```

## ✅ Action Items ☑️

* Implement the pseudocode in a chosen programming language (e.g., Python, Java, C++).
* Test the solution with various input arrays, including edge cases (empty array, array with all zeros, array with no zeros).
* Optimize the code for efficiency and readability.
* Consider alternative approaches to solving the problem and compare their performance.
