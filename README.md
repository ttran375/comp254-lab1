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
