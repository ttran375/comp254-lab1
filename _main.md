# Week 4 Lab Session document

This document provides the necessary instructions for completing the
Week 4 lab exercises.

## Exercise 1: Counting Primitive Operations

Count the primitive operations for the following algorithms/methods:

```python
def main():
    n = 1000
    print("Hey - your input is:", n)
    print("Hmm.. I'm doing more stuff with:", n)
    print("And more:", n)

    i = 1
    while i < n:
        print("Hey - I'm busy looking at:", i)
        i *= 2

    for i in range(1, n + 1):
        j = 1
        while j < n:
            print("Hey - I'm busy looking at:", i, "and", j)
            j *= 2
```

### Detailed Counting

1. **Initialization:**
   - `n = 1000`: 1 operation
   - 3 `print` statements: 3 operations

2. **First While Loop:**
   - `i = 1`: 1 operation
   - `while i < n:`: log2(1000) comparisons (since `i` doubles each time):
        - `print("Hey - I'm busy looking at:", i)`: log2(1000) print operations
        - `i *= 2`: log2(1000) assignments

   The value of log2(1000) is approximately 10 (since 2^10 = 1024).

3. **For Loop and Nested While Loop:**
   - `for i in range(1, n + 1)`: n iterations (n = 1000)
   - `j = 1`: n assignments
   - `while j < n`: n * log2(n) comparisons (since `j` doubles each time for each `i`)
   - `print("Hey - I'm busy looking at:", i, "and", j)`: n * log2(n) print operations
   - `j *= 2`: n * log2(n) assignments

### Total Primitive Operations

- Initialization: 4 operations (1 assignment + 3 prints)
- First While Loop: \( 3 \times 10 = 30 \) operations (10 comparisons + 10 prints + 10 assignments)
- For Loop and Nested While Loop:
  - For Loop: \( 1000 \) iterations
  - Nested While Loop: \( 1000 \times 10 = 10000 \) operations (10000 comparisons + 10000 prints + 10000 assignments)

Total operations:

- Initialization: 4
- First While Loop: 30
- For Loop and Nested While Loop: \( 1000 + 10000 + 10000 + 10000 = 31000 \)

### Grand Total

The total number of primitive operations is \( 4 + 30 + 31000 = 31034 \).
