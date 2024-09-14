% Number of boats and time slots
int: N;  % Number of boats
int: T;  % Number of time slots

% Sets
set of int: Boats = 1..N;
set of int: TimeSlots = 1..T;

% Decision variable: visits[i, t] is the host boat visited by boat i in time slot t
array[Boats, TimeSlots] of var Boats: visits;

% Constraints

% No boat can visit itself
constraint forall(i in Boats, t in TimeSlots) (
    visits[i,t] != i
);

% A host can only host one guest at a time (no double-booking)
constraint forall(j in Boats, t in TimeSlots) (
    forall(i1 in Boats, i2 in Boats where i1 != i2) (
        visits[i1, t] != visits[i2, t]
    )
);

% Weakened constraint: A boat should not visit the same host in consecutive time slots
constraint forall(i in Boats, t in 1..T-1) (
    visits[i, t] != visits[i, t+1]
);

% Solve for a valid assignment of visits
solve satisfy;

% Output the solution
output [
  "Boat " ++ show(i) ++ ": " ++
  join(", ", [ "T" ++ show(t) ++ " -> Host " ++ show(visits[i, t]) | t in TimeSlots ]) ++ "\n"
  | i in Boats
];
