# House-Painting-Problem
## Problem Definition

You are a house painter available from day 1 to n (inclusive). Each house takes one day to paint, and you are given m houses. For each house i (1 to m), you have startDayi and endDayi, where the house can only be painted between startDayi and endDayi (inclusive). The houses are already sorted primarily on startDay and secondarily on endDay (in case of startDay equality). Your task is to find the maximum number of houses that can be painted.

## Repository Overview

This repository contains a collection of different greedy algorithms designed to solve the house painting problem. These algorithms were developed as part of the Analysis of Algorithm Class, offering various strategies to optimize the painting schedule and maximize the number of painted houses.


## Steps to run
### 1. Using makefile
- Execute **"make"** command.
   ```
   $ make
   ```
- Execute **"make run#"** command to run a particular strategy.
   - For example, to execute STRAT1
   ```
   $ make run1
   ```
   - To execute the optimal implementation of STRAT4
   ```
   $ make run5
   ```
### 2. Without using makefile
    
   - To execute STRAT1
     ```
     $ python3 main.py STRAT1
     ```
## Algorithms Included
### STRAT 1
- Iterate over each day starting from day 1 . . . n. For each day, among the 
unpainted houses that are available to be painted on that day, paint the house 
that started being **available the earliest**.
- Time complexity: θ(n) and a space complexity: O(m).

### STRAT 2
- Iterate over each day starting from day 1 . . . n. For each day, among the 
unpainted houses that are available that day, paint the house that started being 
**available the latest**.
- Time Complexity: O(n+m*log(m)) and space complexity : O(m).

### STRAT 3
- Iterate over each day starting from day 1 . . . n. For each day, among the unpainted 
houses that are available that day, paint the house that is **available for the shortest 
duration**.
- Time Complexity: O(n+m*log(m)) and space complexity: O(m).

### STRAT 4
- Iterate over each day starting from day 1 . . . n. For each day, among the 
unpainted houses that are available that day, paint the house that **will stop 
being available the earliest**.

### STRAT 4 OPTIMAL
- Θ(mlog(m)) algorithm based on the greedy strategy

## Experimental Comparitive Study

- Figure 1 depicts the number of houses that can be painted by each strategy. We generated datasets ranging from n = 1000 to 5000 and executed various strategies on these datasets where n equals m.
- Figure 2 represents the running time of each strategy for input size n = 1000 to 5000.
  
 *No of Houses Vs Input Size*

  ![No of Houses Vs Input Size](./Experimental_Comparision/No.ofHouses_Vs_Input_Size.PNG)
 
  *Running Time Vs Input Size*

  ![Running Time Vs Input Size](./Experimental_Comparision/RunningTime_Vs_InputSize.PNG)


## Implementation Details
For detailed implementation information, please refer to the [project report](ProjectReport.pdf).


