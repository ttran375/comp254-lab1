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

## Exercise 2: Big O descriptions

**Describe the following Big O notations for algorithm runtimes:**

**O(1)** – the algorithm has a constant execution time

**O(n)** – the algorithm's execution time increases linearly with the size of the input

**O(logn)** – the algorithm's execution time increases logarithmically with the size of the input

**O(nlogn)** – the algorithm's execution time increases in a manner proportional to n multiplied by log n

**O(n^2)** – the algorithm's execution time increases quadratically with the size of the input

**O(n^3)** – the algorithm's execution time increases cubically with the size of the input

**O(2^n)** – the algorithm's execution time doubles with each additional element in the input data set

**O(n!)** – the algorithm's execution time grows factorially with the size of the input

## Exercise 3: Big O Examples

Recall the definition: f(n) \<= c\* g(n) for n \>=n<sub>0</sub>

**Let** f(n) = 2\*n + 10.

Calculate **c** and **n<sub>0</sub>**<sub>.</sub>

Do the same for the following functions:

1. 15\*n -2

2. 7\*log n – 5

3. 10\* n<sup>3</sup> + 15\*n<sup>2</sup> -15

4. 2*n*<sup>4</sup> +7*n*<sup>3</sup>- 5*n*<sup>2</sup> + 2*n* - 7

$$ f(n) \leq c \cdot g(n) \quad \text{for all} \quad n \geq n_0 $$

### 1. $f(n) = 2n + 10$

We need to find $c$ and $n_0$ such that:

$$ 2n + 10 \leq c \cdot n $$

For $n \geq n_0$, let's choose $n_0 = 10$.

$$ 2n + 10 \leq c \cdot n $$
$$ 2 + \frac{10}{n} \leq c $$

When $n \geq 10$:

$$ 2 + 1 \leq c $$
$$ c \geq 3 $$

Thus, $c = 3$ and $n_0 = 10$ are valid choices.

### 2. $f(n) = 15n - 2$

We need to find $c$ and $n_0$ such that:

$$ 15n - 2 \leq c \cdot n $$

For $n \geq n_0$, let's choose $n_0 = 1$.

$$ 15n - 2 \leq c \cdot n $$
$$ 15 - \frac{2}{n} \leq c $$

When $n \geq 1$:

$$ 15 - 2 \leq c $$
$$ c \geq 13 $$

Thus, $c = 15$ and $n_0 = 1$ are valid choices.

### 3. $f(n) = 7 \log n - 5$

We need to find $c$ and $n_0$ such that:

$$ 7 \log n - 5 \leq c \log n $$

For $n \geq n_0$, let's choose $n_0 = 1$.

$$ 7 \log n - 5 \leq c \log n $$
$$ 7 - \frac{5}{\log n} \leq c $$

For $n \geq 10$:

$$ 7 - \frac{5}{\log 10} \leq c $$
$$ 7 - 2.17 \leq c $$
$$ c \geq 4.83 $$

Thus, $c = 7$ and $n_0 = 10$ are valid choices.

### 4. $f(n) = 10n^3 + 15n^2 - 15$

We need to find $c$ and $n_0$ such that:

$$ 10n^3 + 15n^2 - 15 \leq c \cdot n^3 $$

For $n \geq n_0$, let's choose $n_0 = 1$.

$$ 10n^3 + 15n^2 - 15 \leq c \cdot n^3 $$
$$ 10 + \frac{15}{n} - \frac{15}{n^3} \leq c $$

When $n \geq 1$:

$$ 10 + 15 - 15 \leq c $$
$$ c \geq 10 $$

Thus, $c = 10 + \frac{15}{n_0} - \frac{15}{n_0^3}$, which is approximately 25, so $c = 25$ and $n_0 = 1$ are valid choices.

### 5. $f(n) = 2n^4 + 7n^3 - 5n^2 + 2n - 7$

We need to find $c$ and $n_0$ such that:

$$ 2n^4 + 7n^3 - 5n^2 + 2n - 7 \leq c \cdot n^4 $$

For $n \geq n_0$, let's choose $n_0 = 1$.

$$ 2n^4 + 7n^3 - 5n^2 + 2n - 7 \leq c \cdot n^4 $$
$$ 2 + \frac{7}{n} - \frac{5}{n^2} + \frac{2}{n^3} - \frac{7}{n^4} \leq c $$

When $n \geq 1$:

$$ 2 + 7 - 5 + 2 - 7 \leq c $$
$$ c \geq 2 $$

Thus, $c = 2 + \frac{7}{n_0} - \frac{5}{n_0^2} + \frac{2}{n_0^3} - \frac{7}{n_0^4}$, which is approximately 15, so $c = 15$ and $n_0 = 1$ are valid choices.
