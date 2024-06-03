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
        double[] a = new double[n];
        for (int j = 0; j < n; j++) {
            double total = 0;
            for (int i = 0; i <= j; i++) {
                total += x[i];
            }
            a[j] = total / (j + 1);
        }
        return a;
    }

    public static double[] prefixAverage2(double[] x) {
        int n = x.length;
        double[] a = new double[n];
        double total = 0;
        for (int j = 0; j < n; j++) {
            total += x[j];
            a[j] = total / (j + 1);
        }
        return a;
    }
}
```

### Main Method

```java
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
```

1. **Variable initialization and print statements:**
   - `int n = 1000;` (1 operation)
   - `System.out.println("Hey - your input is: " + n);` (1 operation for concatenation + 1 for print)
   - `System.out.println("Hmm.. I'm doing more stuff with: " + n);` (1 operation for concatenation + 1 for print)
   - `System.out.println("And more: " + n);` (1 operation for concatenation + 1 for print)

   Total: $1 + 2 \times 3 = 7$ operations

2. **First for loop:**
   ```java
   for (int i = 1; i < n; i = i * 2) {
       System.out.println("Hey - I'm busy looking at: " + i);
   }
   ```
   - Initialization: `int i = 1;` (1 operation)
   - Loop condition check `i < n` is executed $\log_2 n$ times. Inside the loop: `System.out.println("Hey - I'm busy looking at: " + i);` (1 operation for concatenation + 1 for print, executed $\log_2 n$ times)
   - Update: `i = i * 2;` (1 operation, executed $\log_2 n - 1$ times)

   Total: $1 + \log_2 n \times (1 + 1 + 1) + (\log_2 n - 1) = 1 + 3\log_2 n - 1 = 3\log_2 n$ operations

3. **Second for loop:**
   ```java
   for (int i = 1; i <= n; i++) {
       for (int j = 1; j < n; j = j * 2) {
           System.out.println("Hey - I'm busy looking at: " + i + " and " + j);
       }
   }
   ```
   - Outer loop initialization: `int i = 1;` (1 operation)
   - Outer loop condition check `i <= n` is executed \(n + 1\) times.
   - Inner loop initialization: `int j = 1;` (executed \(n\) times)
   - Inner loop condition check `j < n` is executed \(n \times \log_2 n\) times.
   - Inside the inner loop: `System.out.println("Hey - I'm busy looking at: " + i + " and " + j);` (1 operation for concatenation + 1 for print, executed \(n \times \log_2 n\) times)
   - Inner loop update: `j = j * 2;` (executed \(n \times (\log_2 n - 1)\) times)
   - Outer loop update: `i++` (executed \(n\) times)

   Total: \(1 + (n + 1) \times 1 + n \times (\log_2 n \times 2 + (\log_2 n - 1) \times 1) = 1 + (n + 1) + n \times (2 \log_2 n + \log_2 n - 1) = 2 + n + 3n \log_2 n - n = 2 + 3n \log_2 n\) operations

### `prefixAverage1` Method

```java
public static double[] prefixAverage1(double[] x) {
    int n = x.length;
    double[] a = new double[n];
    for (int j = 0; j < n; j++) {
        double total = 0;
        for (int i = 0; i <= j; i++) {
            total += x[i];
        }
        a[j] = total / (j + 1);
    }
    return a;
}
```

1. **Initialization:**
   - `int n = x.length;` (1 operation)
   - `double[] a = new double[n];` (1 operation)

2. **Outer loop:**
   - Initialization: `int j = 0;` (1 operation)
   - Condition check `j < n` is executed \(n + 1\) times.
   - Initialization `double total = 0;` is executed \(n\) times.
   - Inner loop: condition check `i <= j` is executed \(\frac{n(n + 1)}{2}\) times.
   - Inside the inner loop: `total += x[i];` is executed \(\frac{n(n + 1)}{2}\) times.
   - Outside the inner loop: `a[j] = total / (j + 1);` is executed \(n\) times.
   - Update: `j++` (executed \(n\) times)

   Total: \(1 + 1 + (1 + n + 1) + n + \frac{n(n + 1)}{2} \times 1 + \frac{n(n + 1)}{2} + n \times 1 + n = 2 + 2n + 1 + \frac{n^2 + n}{2} + \frac{n^2 + n}{2} = 3 + 2n + n^2 + n = n^2 + 3n + 3\) operations

### `prefixAverage2` Method

```java
public static double[] prefixAverage2(double[] x) {
    int n = x.length;
    double[] a = new double[n];
    double total = 0;
    for (int j = 0; j < n; j++) {
        total += x[j];
        a[j] = total / (j + 1);
    }
    return a;
}
```

1. **Initialization:**
   - `int n = x.length;` (1 operation)
   - `double[] a = new double[n];` (1 operation)
   - `double total = 0;` (1 operation)

2. **Loop:**
   - Initialization: `int j = 0;` (1 operation)
   - Condition check `j < n` is executed \(n + 1\) times.
   - Inside the loop: `total += x[j];` (executed \(n\) times)
   - Inside the loop: `a[j] = total / (j + 1);` (executed \(n\) times)
   - Update: `j++` (executed \(n\) times)

   Total: \(1 + 1 + 1 + (1 + n + 1) + n + n + n = 3 + 2n + 1 + 3n = 3n + 4\) operations
