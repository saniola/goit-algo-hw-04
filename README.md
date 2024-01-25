# Sorting Algorithms Analysis in Python

## Overview
In this project, we conducted an analysis of three sorting algorithms in Python: Merge Sort, Insertion Sort, and Timsort. The primary focus was on comparing their execution time on different datasets to assess their efficiency.

## Test Results

### Testing Methodology
We employed the `timeit` module to measure the execution time of each algorithm. The tests involved arrays with 1000 elements, and each test was repeated 1000 times for accuracy.

### Results

| Algorithm            | Execution Time                  |
|----------------------|---------------------------------|
| Merge Sort           | 1.1103299579990562              |
| Insertion Sort       | 9.782114125002408               |
| Timsort              | 0.045517459002439864            |

## Conclusions

### Algorithm Efficiency
Timsort demonstrated significantly higher efficiency compared to Merge Sort and Insertion Sort, especially on larger datasets.

### Usage of Built-in Sorting Functions in Python
Programmers commonly opt for built-in sorting algorithms in Python, such as Timsort, due to their exceptional efficiency and optimizations.

### Theoretical Weaknesses of Algorithms
Our empirical findings corroborated the theoretical complexity estimates of the algorithms, highlighting the overall superiority of Timsort in most cases.

This analysis reaffirms that leveraging built-in sorting functions in Python is an optimal choice for a wide range of sorting tasks.
