import random
import copy

def solve():
    rnd0: list = random.sample(range(1, 10), 9) 
    rnd1: list = [rnd0[-1]]+rnd0[0:8]
    rnd2: list = [rnd1[-1]]+rnd1[0:8]
    solution = [rnd0,
              rnd0[3:]+rnd0[:3],
              rnd0[6:]+rnd0[:6],
              rnd1,
              rnd1[3:]+rnd1[:3],
              rnd1[6:]+rnd1[:6],
              rnd2,
              rnd2[3:]+rnd2[:3],
              rnd2[6:]+rnd2[:6]]
    return solution


def create(hard):
    level = {'easy':3, 'medium':4, 'hard':5, 'extreme':6 }
    if hard not in level:
        """ Enter 'Easy','medium','Hard', or 'Extreme'. """
        raise KeyError('Enter Valid Level')
        
    else:
        z = level[hard]
        solution = solve()
        puzzle = copy.deepcopy(solution)
        for i in range(9):
            zero = random.sample(range(0, 9),z) 
            for j in zero:
                puzzle[i][j] = 0
        return puzzle, solution

def display(puzzle):
    top = '* -  -  -  | -  -  -  | -  -  -  *'
    mid = '| -  -  -  | -  -  -  | -  -  -  |'
    print(top)
    print()
    for i in range(9):
        if i % 3 == 0 and i>0:
            print(mid)
            print()
        for j in range(9):
            if j % 3 == 0:
                print('| ',end='')
            print(puzzle[i][j],' ',end='')
            if j == 8:
                print('|')
        print()
    print(top)
