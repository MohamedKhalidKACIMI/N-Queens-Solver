# N-Queens Backtracking Solver ♟️

This repository contains a Python implementation of the classic **N-Queens Problem**. I built this project to demonstrate my understanding of algorithmic logic, recursive functions, and multidimensional data structures (2D lists) in Python.

## The Problem
The goal of the N-Queens problem is to place `N` chess queens on an `N x N` chessboard so that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.

## How it Works
The script uses a **Backtracking Algorithm**. 
1. It tries to place a queen in the first column.
2. It checks if the placement is safe using the `is_safe()` function (which utilizes Python's `zip()` function to check diagonals).
3. It recursively moves to the next column.
4. If it reaches a dead end, it "backtracks" by removing the previous queen and trying a new position.

## Example Output
The script features a custom print function that generates a beautiful Unicode checkerboard to visualize the final solution. For an 8x8 board (`N = 8`), the output looks like this:

```text
   N-Queens Board
  ------------------------
  | ♛  □  ■  □  ■  □  ■  □ |
  | ■  □  ■  □  ♛  □  ■  □ |
  | □  ■  □  ■  □  ■  □  ♛ |
  | ■  □  ■  □  ■  ♛  ■  □ |
  | □  ■  ♛  ■  □  ■  □  ■ |
  | ■  □  ■  □  ■  □  ■  ♛ |
  | □  ♛  □  ■  □  ■  □  ■ |
  | ■  □  ■  ♛  ■  □  ■  □ |
  ------------------------
```

## Technologies Used
* Python 3
* Core Concepts: Variables, Control Flow, Lists, Functions, Recursion.
