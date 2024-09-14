
include "globals.mzn";

var int: cake1;
var int: cake2;

constraint cake1 >= 0;
constraint cake2 >= 0;
constraint 250 * cake1 + 200* cake2 <= 4000;
constraint 2 * cake1 <= 6;
constraint 75 * cake1 + 150 * cake2 <= 2000;
constraint 100 * cake1 + 150 * cake2 <= 500;
constraint 75 * cake2 <= 500;

solve maximize cake1 * 40 + cake2 * 45;

