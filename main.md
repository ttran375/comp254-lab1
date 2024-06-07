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

### Main method

- Initialization: 4 operations (1 assignment + 3 prints)
- First While Loop: $3 \times 10 = 30$ operations (10 comparisons + 10 prints + 10 assignments)
- For Loop and Nested While Loop:
  - For Loop: $1000$ iterations
  - Nested While Loop: $1000 \times 10 = 10000$ operations (10000 comparisons + 10000 prints + 10000 assignments)

The total number of primitive operations is $4 + 30 + 31000 = 31034$.

### prefix_average1

```python
def prefix_average1(x):
    n = len(x)  # 1 assignment
    a = [0] * n  # 1 assignment + n assignments (to initialize the list)
    for j in range(n):  # Outer loop runs n times
        total = 0  # 1 assignment for each j
        for i in range(j + 1):  # Inner loop runs j+1 times
            total += x[i]  # 1 addition + 1 list access per iteration of inner loop
        a[j] = total / (j + 1)  # 1 division + 1 assignment per iteration of outer loop
    return a  # 1 return statement
```

### Detailed Counting

1. **Initialization:**
   - `n = len(x)`: 1 assignment
   - `a = [0] * n`: 1 assignment for list creation + n assignments to initialize the list

2. **Outer Loop (`for j in range(n)`):**
   - Runs `n` times:
     - `total = 0`: 1 assignment per iteration (total of n assignments)

3. **Inner Loop (`for i in range(j + 1)`):**
   - Runs $\sum_{j=0}^{n-1} (j+1)$ times:
     - `total += x[i]`: 1 addition + 1 list access per iteration

4. **Assignment and Division (`a[j] = total / (j + 1)`):**
   - Runs `n` times:
     - 1 division + 1 assignment per iteration

5. **Return Statement:**
   - `return a`: 1 return statement

### Total Primitive Operations

1. **Initialization:**
   - `n = len(x)`: 1 operation
   - `a = [0] * n`: 1 + n operations (1 for list creation + n for list initialization)

2. **Outer Loop:**
   - `for j in range(n)`: 0 comparisons (Python loop overhead, not counting each iteration)
   - `total = 0`: n operations

3. **Inner Loop:**
   - Runs \( \sum_{j=0}^{n-1} (j+1) = \frac{n(n+1)}{2} \) times:
     - `total += x[i]`: \( \frac{n(n+1)}{2} \) operations (additions) + \( \frac{n(n+1)}{2} \) operations (list accesses)

4. **Assignment and Division:**
   - `a[j] = total / (j + 1)`: n divisions + n assignments

5. **Return Statement:**
   - `return a`: 1 operation

### Summing Up

- Initialization: \( 1 + 1 + n = n + 2 \)
- Outer Loop: \( n \)
- Inner Loop: \( \frac{n(n+1)}{2} \) additions + \( \frac{n(n+1)}{2} \) list accesses
- Division and Assignment: \( n + n = 2n \)
- Return: 1

### Grand Total

- Primitive operations: \( (n + 2) + n + \left( \frac{n(n+1)}{2} \right) + \left( \frac{n(n+1)}{2} \right) + 2n + 1 \)
- Simplifying: \( 2n + 2 + \left( \frac{n(n+1)}{2} \right) + \left( \frac{n(n+1)}{2} \right) + 2n + 1 \)
- Further simplification: \( 4n + 3 + n^2 + n \)
- Final form: \( n^2 + 5n + 3 \)

Thus, the total number of primitive operations for the `prefix_average1` function is \( n^2 + 5n + 3 \).
