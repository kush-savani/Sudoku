
A Python Package To Create A Pair Of Solve And Unsolve Sudoku.

# Usage
Import Sudoku In You Code As
```python
from sudoku import *
```
There Are Two Method.
1. create()
2. display()

## 1. create()
Method `create()` Take **level** As A Input Parameter.
**level** Should As
* easy
* medium
* hard
* extreme

And Return A Two Variable **Unsolve Sudoku** And **Solve Sudoku**
```python
Puzzle, Solution = create('easy')
print(Puzzle)
```
```python
[[0, 3, 0, 6, 5, 1, 0, 4, 7],
 [6, 0, 1, 2, 4, 0, 9, 3, 0],
 [2, 4, 7, 9, 3, 8, 0, 0, 0],
 [0, 9, 3, 0, 6, 0, 1, 2, 4],
 [0, 6, 5, 1, 0, 0, 7, 9, 3],
 [1, 2, 4, 0, 9, 3, 0, 0, 5],
 [4, 0, 9, 3, 0, 6, 5, 1, 0],
 [0, 8, 6, 0, 1, 2, 4, 0, 9],
 [5, 1, 0, 4, 7, 9, 0, 8, 0]]
```
```python
print(Solution)
```
```python
[[9, 3, 8, 6, 5, 1, 2, 4, 7],
 [6, 5, 1, 2, 4, 7, 9, 3, 8],
 [2, 4, 7, 9, 3, 8, 6, 5, 1],
 [7, 9, 3, 8, 6, 5, 1, 2, 4],
 [8, 6, 5, 1, 2, 4, 7, 9, 3],
 [1, 2, 4, 7, 9, 3, 8, 6, 5],
 [4, 7, 9, 3, 8, 6, 5, 1, 2],
 [3, 8, 6, 5, 1, 2, 4, 7, 9],
 [5, 1, 2, 4, 7, 9, 3, 8, 6]]
```

Here **Puzzle** Is Unsolve Sudoku In Form Of Matrix. And **Solution** Is Solve Sudoku Of Puzzle.

## 2. display()
Method `display()` Take **Sudoku** As A Input Parameter. Which Chould Be Solve Or Unsolve.
Display **Puzzle**
```python
display(Puzzle)
```
Output:
```python
* -  -  -  | -  -  -  | -  -  -  *

| 0  3  0  | 6  5  1  | 0  4  7  |

| 6  0  1  | 2  4  0  | 9  3  0  |

| 2  4  7  | 9  3  8  | 0  0  0  |

| -  -  -  | -  -  -  | -  -  -  |

| 0  9  3  | 0  6  0  | 1  2  4  |

| 0  6  5  | 1  0  0  | 7  9  3  |

| 1  2  4  | 0  9  3  | 0  0  5  |

| -  -  -  | -  -  -  | -  -  -  |

| 4  0  9  | 3  0  6  | 5  1  0  |

| 0  8  6  | 0  1  2  | 4  0  9  |

| 5  1  0  | 4  7  9  | 0  8  0  |

* -  -  -  | -  -  -  | -  -  -  *
```

Display **Solution**
```python
display(Solution)
```
Output
```python
* -  -  -  | -  -  -  | -  -  -  *

| 9  3  8  | 6  5  1  | 2  4  7  |

| 6  5  1  | 2  4  7  | 9  3  8  |

| 2  4  7  | 9  3  8  | 6  5  1  |

| -  -  -  | -  -  -  | -  -  -  |

| 7  9  3  | 8  6  5  | 1  2  4  |

| 8  6  5  | 1  2  4  | 7  9  3  |

| 1  2  4  | 7  9  3  | 8  6  5  |

| -  -  -  | -  -  -  | -  -  -  |

| 4  7  9  | 3  8  6  | 5  1  2  |

| 3  8  6  | 5  1  2  | 4  7  9  |

| 5  1  2  | 4  7  9  | 3  8  6  |

* -  -  -  | -  -  -  | -  -  -  *
```

**Source Code** [Github](https://github.com/kush-savani/Sudoku.git)