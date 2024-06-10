# 0. Rotate 2D Matrix

## Project Overview

The "0. Rotate 2D Matrix" project involves implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a solid understanding of matrix manipulation and in-place operations in Python.

## Key Concepts

### Matrix Representation in Python

- **Lists of Lists**: 2D matrices in Python are represented using lists of lists.
- **Access and Modification**: Learn to access and modify elements within a 2D matrix.

### In-place Operations

- **Definition**: Performing operations directly on the data without creating a copy.
- **Importance**: Minimizes space complexity by modifying the original matrix.

### Matrix Transposition

- **Concept**: Swapping rows with columns in a matrix.
- **Implementation**: An essential step in rotating the matrix.

### Reversing Rows in a Matrix

- **Manipulation**: Reversing the order of elements in each row to complete the rotation.

### Nested Loops

- **Usage**: Iterating through 2D data structures.
- **Modification**: Altering elements within nested loops to achieve the desired rotation.

## Resources

### Python Official Documentation

- **Data Structures**: [List comprehensions, nested list comprehension](https://docs.python.org/3/tutorial/datastructures.html)
- **More on Lists**: [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

### GeeksforGeeks Articles

- **Inplace Rotate Square Matrix by 90 Degrees**: [Article](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- **Transpose a Matrix in Single Line in Python**: [Article](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

### TutorialsPoint

- **Python Lists**: [Basics of List Manipulation in Python](https://www.tutorialspoint.com/python/python_lists.htm)

By understanding these concepts and utilizing the provided resources, you can methodically approach the problem. First, transpose the matrix, and then reverse each row to achieve a 90-degree clockwise rotation. This project will enhance your problem-solving and algorithmic thinking skills in Python.

## Requirements

### General

- **Allowed Editors**: vi, vim, emacs
- **Execution Environment**: Ubuntu 20.04 LTS using python3 (version 3.8.10)
- **File Format**: All files should end with a new line.
- **Shebang Line**: The first line of all files should be exactly `#!/usr/bin/python3`
- **README.md**: A mandatory file at the root of the project folder.
- **Coding Style**: Your code should follow the `pycodestyle` style (version 2.8.0)
- **Module Restrictions**: You are not allowed to import any module.
- **Documentation**: All modules and functions must be documented.
- **Executable Files**: All files must be executable.

## project

Given an n x n 2D matrix, rotate it 90 degrees clockwise:

- Prototype: def rotate_2d_matrix(matrix):
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.
