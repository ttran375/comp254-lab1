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

- Initialization: 4 operations (1 assignment + 3 prints)
- First While Loop: $3 \times 10 = 30$ operations (10 comparisons + 10 prints + 10 assignments)
- For Loop and Nested While Loop:
  - For Loop: $1000$ iterations
  - Nested While Loop: $1000 \times 10 = 10000$ operations (10000 comparisons + 10000 prints + 10000 assignments)

The total number of primitive operations is $4 + 30 + 31000 = 31034$.
