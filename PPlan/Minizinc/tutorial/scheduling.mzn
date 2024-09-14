
include "globals.mzn";

var 1..3: T1;
var 1..3: T2;
var 1..3: T3;
var 1..3: T4;
var 1..3: T5;


constraint T1 > T3;
constraint T3 < T4;
constraint T3 > T5;
constraint T2 != T1;
constraint T2 != T4;
constraint T4 != 2;


solve satisfy