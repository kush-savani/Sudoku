
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
```
Here **Puzzle** Is Unsolve Sudoku In Form Of Matrix. And **Solution** Is Solve Sudoku Of Puzzle.

## 2. display()
Method `display()` Take **Sudoku** As A Input Parameter. Which Chould Be Solve Or Unsolve.

```python
display(puzzle)
```
![Image of Yaktocat](https://drive.google.com/open?id=144uoHVccelCP82ci7dCzg3IY2bZxRn5e)


```python
display(solution)
```
![Image of Yaktocat](https://drive.google.com/open?id=1TtzDXUeRNT3EOTaOUHysA71EO0_hyZuz)


**Source Code** [Github](https://github.com/kush-savani/Sudoku.git)