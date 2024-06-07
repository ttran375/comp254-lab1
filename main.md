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

- Initialization: $1 + 1 + n = n + 2$
- Outer Loop: $n$
- Inner Loop: $\frac{n(n+1)}{2}$ additions + $\frac{n(n+1)}{2}$ list accesses
- Division and Assignment: $n + n = 2n$
- Return: 1

Primitive operations: $(n + 2) + n + \left( \frac{n(n+1)}{2} \right) + \left( \frac{n(n+1)}{2} \right) + 2n + 1 = n^2 + 5n + 3$

## prefix_average2

```python
def prefix_average2(x):
    n = len(x)  # 1 assignment
    a = [0] * n  # 1 assignment + n assignments (to initialize the list)
    total = 0  # 1 assignment
    for j in range(n):  # Outer loop runs n times
        total += x[j]  # 1 addition + 1 list access per iteration
        a[j] = total / (j + 1)  # 1 division + 1 assignment per iteration
    return a  # 1 return statement
```

- Initialization: \( 1 + 1 + n + 1 = n + 3 \)
- Outer Loop (per iteration): \( 3 \) operations (1 addition + 1 list access + 1 division + 1 assignment)
- Total for Outer Loop: \( 3n \)
- Return: 1

Primitive operations: $(n + 3) + 3n + 1 = 4n + 4$
