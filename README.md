# Week 4 Lab Session document

This document provides the necessary instructions for completing the
Week 4 lab exercises.

## Exercise 1: Counting Primitive Operations

Count the primitive operations for the following algorithms/methods:

``` java
public class Main {
    public static void main(String[] args) {
        int n = 1000;
        System.out.println("Hey - your input is: " + n);
        System.out.println("Hmm.. I'm doing more stuff with: " + n);
        System.out.println("And more: " + n);

        for (int i = 1; i < n; i = i * 2) {
            System.out.println("Hey - I'm busy looking at: " + i);
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j < n; j = j * 2) {
                System.out.println("Hey - I'm busy looking at: " + i + " and " + j);
            }
        }
    }

    public static double[] prefixAverage1(double[] x) {
        int n = x.length;
        double[] a = new double[n]; // filled with zeros by default
        for (int j = 0; j < n; j++) {
            double total = 0; // begin computing x[0] + ... + x[j]
            for (int i = 0; i <= j; i++) {
                total += x[i];
            }
            a[j] = total / (j + 1); // record the average
        }
        return a;
    }

    public static double[] prefixAverage2(double[] x) {
        int n = x.length;
        double[] a = new double[n]; // filled with zeros by default
        double total = 0; // compute prefix sum as x[0] + x[1] + ...
        for (int j = 0; j < n; j++) {
            total += x[j]; // update prefix sum to include x[j]
            a[j] = total / (j + 1); // compute average based on current sum
        }
        return a;
    }
}
```

## Exercise 2: Big O descriptions

**Describe the following Big O notations for algorithm runtimes:**

Sure! Here are the descriptions of the given Big O notations for algorithm runtimes:

**O(1)** – the algorithm has a constant execution time: The execution time of the algorithm remains constant, regardless of the size of the input data set.

**O(n)** – the algorithm's execution time increases linearly with the size of the input: If the input size doubles, the execution time also doubles. This is common in simple loops that iterate over all elements.

**O(logn)** – the algorithm's execution time increases logarithmically with the size of the input: The execution time grows slowly as the input size increases. This is typical in divide-and-conquer algorithms like binary search.

**O(nlogn)** – the algorithm's execution time increases in a manner proportional to n multiplied by log n: This is often seen in efficient sorting algorithms like mergesort and heapsort.

**O(n^2)** – the algorithm's execution time increases quadratically with the size of the input: If the input size doubles, the execution time increases by four times. This is common in algorithms with nested loops iterating over the data set, such as bubble sort and selection sort.

**O(n^3)** – the algorithm's execution time increases cubically with the size of the input: If the input size doubles, the execution time increases by eight times. This is seen in algorithms with three nested loops iterating over the data set, such as certain matrix multiplication algorithms.

**O(2^n)** – the algorithm's execution time doubles with each additional element in the input data set: This represents exponential growth, where even small increases in the input size result in a dramatic increase in execution time. This is typical in recursive algorithms that solve problems by breaking them down into smaller subproblems, like the naive implementation of the Fibonacci sequence.

**O(n!)** – the algorithm's execution time grows factorially with the size of the input: This is the most extreme case of growth, where the execution time increases extremely rapidly with the input size. This is seen in algorithms that generate all permutations of a set, such as the brute-force approach to the traveling salesman problem.

## Exercise 3: Big O Examples

Recall the definition: f(n) \<= c\* g(n) for n \>=n<sub>0</sub>

**Let** f(n) = 2\*n + 10.

Calculate **c** and **n<sub>0</sub>**<sub>.</sub>

Do the same for the following functions:

1. 15\*n -2

2. 7\*log n – 5

3. 10\* n<sup>3</sup> + 15\*n<sup>2</sup> -15

4. 2*n*<sup>4</sup> +7*n*<sup>3</sup>- 5*n*<sup>2</sup> + 2*n* - 7

To determine the constants $c$ and $n_0$ such that $f(n) \leq c \cdot g(n)$ for $n \geq n_0$, we typically identify $g(n)$ as a function that asymptotically bounds $f(n)$. This involves comparing the given function $f(n)$ with a simpler function $g(n)$ that grows at a comparable rate.

### 1. $f(n) = 2n + 10$

We choose $g(n) = n$.

$$ f(n) \leq c \cdot g(n) $$
$$ 2n + 10 \leq c \cdot n $$

For $n \geq n_0$:

$$ 2n + 10 \leq c \cdot n $$
$$ 2 + \frac{10}{n} \leq c $$

As $n \to \infty$, $\frac{10}{n} \to 0$. We can choose $c = 3$ and determine $n_0$:

$$ 2 + \frac{10}{n_0} \leq 3 $$
$$ \frac{10}{n_0} \leq 1 $$
$$ n_0 \geq 10 $$

Thus, $c = 3$ and $n_0 = 10$.

### 2. $f(n) = 15n - 2$

We choose $g(n) = n$.

$$ f(n) \leq c \cdot g(n) $$
$$ 15n - 2 \leq c \cdot n $$

For $n \geq n_0$:

$$ 15 - \frac{2}{n} \leq c $$

As $n \to \infty$, $\frac{2}{n} \to 0$. We can choose $c = 15$ and determine $n_0$:

$$ 15 - \frac{2}{n_0} \leq 15 $$
$$ n_0 \geq 1 $$

Thus, $c = 15$ and $n_0 = 1$.

### 3. $f(n) = 7 \log n - 5$

We choose $g(n) = \log n$.

$$ f(n) \leq c \cdot g(n) $$
$$ 7 \log n - 5 \leq c \cdot \log n $$

For $n \geq n_0$:

$$ 7 - \frac{5}{\log n} \leq c $$

As $n \to \infty$, $\frac{5}{\log n} \to 0$. We can choose $c = 7$ and determine $n_0$:

$$ 7 - \frac{5}{\log n_0} \leq 7 $$
$$ \frac{5}{\log n_0} \leq 0 $$

This implies we need $\log n_0 \geq 1$, or $n_0 \geq e \approx 2.718$.

Thus, $c = 7$ and $n_0 \geq 3$.

### 4. $f(n) = 10n^3 + 15n^2 - 15$

We choose $g(n) = n^3$.

$$ f(n) \leq c \cdot g(n) $$
$$ 10n^3 + 15n^2 - 15 \leq c \cdot n^3 $$

For $n \geq n_0$:

$$ 10 + \frac{15}{n} - \frac{15}{n^3} \leq c $$

As $n \to \infty$, $\frac{15}{n} \to 0$ and $\frac{15}{n^3} \to 0$. We can choose $c = 11$ and determine $n_0$:

$$ 10 + \frac{15}{n_0} - \frac{15}{n_0^3} \leq 11 $$
$$ \frac{15}{n_0} - \frac{15}{n_0^3} \leq 1 $$

Since $\frac{15}{n_0}$ dominates $\frac{15}{n_0^3}$ for large $n_0$, solving $\frac{15}{n_0} \leq 1$ gives:

$$ n_0 \geq 15 $$

Thus, $c = 11$ and $n_0 = 15$.

### 5. $f(n) = 2n^4 + 7n^3 - 5n^2 + 2n - 7$

We choose $g(n) = n^4$.

$$ f(n) \leq c \cdot g(n) $$
$$ 2n^4 + 7n^3 - 5n^2 + 2n - 7 \leq c \cdot n^4 $$

For $n \geq n_0$:

$$ 2 + \frac{7}{n} - \frac{5}{n^2} + \frac{2}{n^3} - \frac{7}{n^4} \leq c $$

As $n \to \infty$, the fractions approach 0. We can choose $c = 3$ and determine $n_0$:

$$ 2 + \frac{7}{n_0} - \frac{5}{n_0^2} + \frac{2}{n_0^3} - \frac{7}{n_0^4} \leq 3 $$

For large $n_0$, solving $2 + \frac{7}{n_0} \leq 3$:

$$ \frac{7}{n_0} \leq 1 $$
$$ n_0 \geq 7 $$

Thus, $c = 3$ and $n_0 = 7$.

### Summary

1. $f(n) = 2n + 10$: $c = 3$, $n_0 = 10$
2. $f(n) = 15n - 2$: $c = 15$, $n_0 = 1$
3. $f(n) = 7 \log n - 5$: $c = 7$, $n_0 = 3$
4. $f(n) = 10n^3 + 15n^2 - 15$: $c = 11$, $n_0 = 15$
5. $f(n) = 2n^4 + 7n^3 - 5n^2 + 2n - 7$: $c = 3$, $n_0 = 7$

## Exercise 4: Asymptotic Analysis and Big O notation

**What is the growth rate for the following functions? Express it in
terms of Big Oh notation:**

1. All the examples of exercise 1

2. 1000\*n + 1

3. n ( n-1000)

4. 100\* (n-1)<sup>3</sup> - 10\*(n<sup>2</sup> -15) + 3n -10000

5. (n-10)\*(n+15) + 100000

6. 2n+100log n

7. 3logn+2 is O(logn)

8. 20n3 +10nlog n+5 is O(n3)

## Exercise 5: Asymptotic growth rate

Order the following functions by asymptotic growth rate.

> 4nlogn+2n, 2<sup>10</sup> , 2<sup>logn</sup> . 3n+100logn, 4n,
> 2<sup>n</sup> , n<sup>2</sup>+10n, n<sup>3</sup> ,nlogn

Hint: Simplify the expressions, and then use the ordering of the seven
important algorithm-analysis functions to order this set.
