# 📚 Data Structures and Algorithms: Key Takeaways

> This document summarizes key concepts and algorithms from "Data Structures and Algorithms: Annotated Reference with Examples" by Granville Barnett and Luca Del Tongo.  It focuses on practical implementations and emphasizes the importance of Big O notation and testing for efficient software development.


## 🧠 Core Concepts 

### 🤔 Big O Notation

*   **O(1):** Constant time; independent of input size (e.g., adding to a linked list's tail).
*   **O(n):** Linear time; proportional to input size (e.g., searching a linked list).
*   **O(log n):** Logarithmic time; typically associated with algorithms that divide the problem (e.g., searching a balanced binary search tree).
*   **O(n log n):**  Common in algorithms that divide and conquer then merge (e.g., merge sort).
*   **O(n²):** Quadratic time (e.g., bubble sort).
*   **O(n³):** Cubic time; very rare.
*   **O(2ⁿ):** Exponential time; incredibly rare.  Avoid if possible!

*   Big O notation helps compare algorithm growth, independent of hardware.  A logarithmic algorithm will always outperform a quadratic one for sufficiently large datasets.
*   It's a crucial communication tool for discussing algorithm efficiency.


### 💻 Imperative Programming

*   All examples are in pseudocode easily ported to C++, C#, and Java.
*   Familiarity with imperative programming constructs is essential.
*   Functional programmers will need to adapt the examples to their chosen language.
*   C# and Java's managed environments (garbage collection) simplifies memory management compared to C++.


### 🧱 Object-Oriented Concepts

*   Understanding *inheritance*, *encapsulation*, and *polymorphism* is beneficial for grasping data structure designs.
*   Familiarity with *interfaces* is helpful for the C# examples.


### 📝 Pseudocode Style

*   Algorithms include `Pre` and `Post` conditions.
*   Parameter types are inferred from context.
*   Explicit language construct endings (e.g., `end for`).
*   `yield` keyword returns values one at a time to the caller.


## 🌳 Data Structures

### ⛓️ Linked Lists

*   **Singly Linked List:**  Each node points to the next.  Insertion at head/tail is O(1), but random insertion is O(n). Searching and deletion are O(n).  Dynamic resizing is an advantage.
    *   **Insertion:**  O(1) at head/tail, O(n) otherwise.
    *   **Searching:** O(n).
    *   **Deletion:** O(n).
    *   **Traversal:** O(n).
    *   **Reverse Traversal:** O(n²).
*   **Doubly Linked List:** Each node points to the next and previous node.  Offers efficient O(1) insertion, deletion, and reverse traversal.  Searching remains O(n).

### 🌲 Binary Search Tree (BST)

*   Nodes are ordered: left subtree < node < right subtree.
*   Operations (insertion, search, deletion) are O(log n) for balanced trees.  Unbalanced trees degrade to O(n).
    *   **Insertion:** O(log n) (balanced).
    *   **Searching:** O(log n) (balanced).
    *   **Deletion:** O(log n) (balanced).  Four cases to consider (leaf node, one child, two children).
    *   **Tree Traversals:** Preorder, Postorder, Inorder (O(n)), Breadth-First (O(n)).  Inorder traversal yields values in sorted order.

### HEAP ⛰️

*   Min-heap: Parent node ≤ children. Max-heap: Parent node ≥ children.  Typically implemented as an array.
    *   **Insertion:** O(log n).
    *   **Deletion:** O(log n).
    *   **Searching:** O(n) (naive), Optimized search attempts to leverage heap properties for faster detection of non-existence (but still O(n) worst case).
    *   **Traversal:** O(n).

### 🧮 Sets

*   Unordered Set: Members are unique, no specific order. Efficiently implemented using hash tables (O(1) insertion and near O(1) lookup).
*   Ordered Set: Members are unique and ordered according to a comparison function. Implemented using AVL trees (logarithmic operations).


## ⚙️ Algorithms

### 🔀 Sorting Algorithms

*   **Bubble Sort:** O(n²). Simple but inefficient.
*   **Merge Sort:** O(n log n). Divide and conquer, efficient.
*   **Quick Sort:** O(n log n) (average case).  Divide and conquer, pivot selection crucial for performance. O(n²) worst case.
*   **Insertion Sort:** O(n²).  Efficient for small datasets or nearly sorted data.
*   **Shell Sort:** O(n log²n). Improved insertion sort.
*   **Radix Sort:**  Uses buckets to sort based on keys (digits). Efficient for integers.


### 🔢 Numeric Algorithms

*   **Primality Test:** Determines if a number is prime.
*   **Base Conversions:** Converts base 10 numbers to binary, octal, hexadecimal.
*   **Greatest Common Denominator (GCD):** Euclid's algorithm.
*   **Maximum Value (N digits, base B):** Calculates the maximum value for a given base and number of digits (Bⁿ⁻¹).
*   **Factorial:** Iterative implementation.


### 🔎 Searching Algorithms

*   **Sequential Search:** O(n). Simple linear search.
*   **Probability Search:** O(n).  A statistical sequential search that improves performance for frequently accessed items.


### 🧵 String Algorithms

*   **Reverse Words:** Reverses the order of words in a sentence.
*   **Palindrome Detection:** Checks if a string is a palindrome.
*   **Word Count:** Counts the number of words in a string.
*   **Repeated Word Count:** Counts the number of repeated words.
*   **First Matching Character:** Finds the index of the first matching character between two strings.


## ✅ Action Items

*   Review and understand the Big O notation complexities for each algorithm and data structure.
*   Implement the pseudocode algorithms in your preferred imperative language.
*   Write unit tests for each implementation to verify correctness and edge cases.
*   Explore the provided links to learn more about the mentioned testing frameworks and libraries.
*   Experiment with different data structures and algorithms to solve various problems.

