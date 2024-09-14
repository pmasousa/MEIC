include "globals.mzn";

int: n = 15;  % Size of the chessboard (4x4)

% Decision variable: Queen positions in each row (one queen per row)
array[1..n] of var 1..n: queens;

% Constraint: No two queens in the same column
constraint all_different(queens);

% Constraint: No two queens on the same diagonal (major and minor diagonals)
constraint all_different([queens[i] + i | i in 1..n]);  % Major diagonals
constraint all_different([queens[i] - i | i in 1..n]);  % Minor diagonals

% Solve: Find all solutions where the queens are placed
solve satisfy;

% Output: Display the queen positions in a chessboard-like format
output [
    "Solution:\n"
] ++ [
    concat([ if fix(queens[i]) == j then "Q " else ". " endif | j in 1..n ]) ++ "\n"
    | i in 1..n
] ++ ["\n"];
