include "globals.mzn";

var 1..9: S;
var 1..9: M;
var 0..9: E;
var 0..9: N;
var 0..9: D;
var 0..9: O;
var 0..9: R;
var 0..9: Y;

constraint 1000 * S + 100 * E + 10 * N + D + 1000 * M + 100 * O + 10 * R + E = 10000 * M + 1000 * O + 100 * N + 10 * E +Y;

constraint alldifferent([S, M, E, N, D, O, R, Y]);

solve satisfy
