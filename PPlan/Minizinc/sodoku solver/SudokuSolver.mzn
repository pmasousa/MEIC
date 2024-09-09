% Sudoku Solver in MiniZinc
include "globals.mzn";

% Get the size of the Sudoku grid from the input file
int: n;

% Calculate sqrt(n) once and reuse it
int: sqrt_n = round(sqrt(n));

% A n x n array for Sudoku cells
array[1..n, 1..n] of var 1..n: grid;

% Load the given Sudoku puzzle (0 represents an empty cell)
array[1..n, 1..n] of int: puzzle;

% Constraints to fill pre-defined numbers (puzzle clues)
constraint
    forall(i, j in 1..n where puzzle[i,j] != 0) (
        grid[i,j] = puzzle[i,j]
    );

% Row constraints: Each row must contain distinct values
constraint
    forall(i in 1..n) (
        alldifferent([grid[i,j] | j in 1..n])
    );

% Column constraints: Each column must contain distinct values
constraint
    forall(j in 1..n) (
        alldifferent([grid[i,j] | i in 1..n])
    );

% Subgrid constraints: Each sqrt(n) x sqrt(n) subgrid must contain distinct values
constraint
    forall(r, c in 0..sqrt_n-1) (
        alldifferent([grid[sqrt_n*r + i, sqrt_n*c + j] | i, j in 1..sqrt_n])
    );

% Symmetry breaking: Fix the first cell to reduce search space
% This assumes that the first cell (1, 1) is empty in the puzzle.
constraint grid[1, 1] <= grid[n, n];

% Solve: Find a solution using a more explicit search strategy
solve :: int_search([grid[i,j] | i in 1..n, j in 1..n], input_order, indomain_min, complete) satisfy;

% Output the solution as a grid
output [
    if j = n then show(grid[i,j]) ++ "\n"
    else show(grid[i,j]) ++ " "
    endif
    | i in 1..n, j in 1..n
];
