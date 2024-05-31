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

To count the primitive operations in the given code, we'll identify the number of operations performed in each part of the code. Primitive operations include assignments, comparisons, arithmetic operations, and method calls like `System.out.println`.

Let's break it down step by step.

### Code Analysis

```java
public static void main(String[] args) {
    int n = 1000; // 1 assignment
    System.out.println("Hey - your input is: " + n); // 1 concatenation, 1 method call
    System.out.println("Hmm.. I'm doing more stuff with: " + n); // 1 concatenation, 1 method call
    System.out.println("And more: " + n); // 1 concatenation, 1 method call

    for (int i = 1; i < n; i = i * 2) { // Loop with initialization, comparison, multiplication, assignment
        System.out.println("Hey - I'm busy looking at: " + i); // 1 concatenation, 1 method call
    }

    for (int i = 1; i <= n; i++) { // Outer loop with initialization, comparison, increment, assignment
        for (int j = 1; j < n; j = j * 2) { // Inner loop with initialization, comparison, multiplication, assignment
            System.out.println("Hey - I'm busy looking at: " + i + " and " + j); // 2 concatenations, 1 method call
        }
    }
}
```

### Detailed Primitive Operation Count

1. **Initialization and Assignments:**
   - `int n = 1000;` : 1 operation
   - `for (int i = 1; i < n; i = i * 2) {` : 1 initialization
   - `for (int i = 1; i <= n; i++) {` : 1 initialization
   - `for (int j = 1; j < n; j = j * 2) {` : 1 initialization

2. **Comparisons:**
   - `i < n` in the first loop: \(\log_2 n\) comparisons
   - `i <= n` in the outer loop: \(n\) comparisons
   - `j < n` in the inner loop: \(n \times \log_2 n\) comparisons

3. **Increment/Multiplications and Assignments:**
   - `i = i * 2` in the first loop: \(\log_2 n\) multiplications, \(\log_2 n\) assignments
   - `i++` in the outer loop: \(n\) increments, \(n\) assignments
   - `j = j * 2` in the inner loop: \(n \times \log_2 n\) multiplications, \(n \times \log_2 n\) assignments

4. **Method Calls and String Concatenations:**
   - `System.out.println("Hey - your input is: " + n);`: 1 concatenation, 1 method call
   - `System.out.println("Hmm.. I'm doing more stuff with: " + n);`: 1 concatenation, 1 method call
   - `System.out.println("And more: " + n);`: 1 concatenation, 1 method call
   - `System.out.println("Hey - I'm busy looking at: " + i);` inside first loop: \(\log_2 n\) concatenations, \(\log_2 n\) method calls
   - `System.out.println("Hey - I'm busy looking at: " + i + " and " + j);` inside nested loop: \(2 \times n \times \log_2 n\) concatenations, \(n \times \log_2 n\) method calls

### Total Primitive Operations

Summing up all the operations:

1. **Assignments:**
   - $1 + 1 + 1 + \log_2 n + n + n \times \log_2 n + \log_2 n = 2 + 2\log_2 n + n + n \times \log_2 n$

2. **Comparisons:**
   - $\log_2 n + n + n \times \log_2 n = n + 2n \log_2 n$

3. **Increments/Multiplications:**
   - $\log_2 n + \log_2 n + n + n \times \log_2 n = n + 3\log_2 n + n \times \log_2 n$

4. **Concatenations and Method Calls:**
   - $1 + 1 + 1 + \log_2 n + 2 \times n \times \log_2 n + n \times \log_2 n = 3 + 3 \times \log_2 n + 3 \times n \times \log_2 n$

Combining all types of operations:

\[ 2 + 2 \log_2 n + n + n \times \log_2 n + n + 2 n \log_2 n + n + 3 \log_2 n + n \times \log_2 n + 3 + 3 \log_2 n + 3 \times n \times \log_2 n \]

Simplifying, we get:

\[ \text{Total Operations} = \mathcal{O}(n \log n) \]

Therefore, the total number of primitive operations is dominated by $n \log n$, indicating an overall time complexity of $\mathcal{O}(n \log n)$.

## Exercise 2: Big O descriptions

**Describe the following Big O notations for algorithm runtimes:**

**O(1) –** the algorithm has a constant execution time

**O(n) -**

**O(logn) -**

**O(nlogn) -**

**O(n^2) –**

**O(n^3) -**

**O(2^n) -**

**O(n!) -**

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
