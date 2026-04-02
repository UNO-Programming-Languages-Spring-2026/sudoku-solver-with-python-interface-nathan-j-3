row(1..9).
col(1..9).
num(1..9).

% Each cell has exactly one number
1 { sudoku(R,C,N) : num(N) } 1 :- row(R), col(C).

% Row constraints
:- row(R), num(N), #count { C : sudoku(R,C,N) } != 1.

% Column constraints
:- col(C), num(N), #count { R : sudoku(R,C,N) } != 1.

% 3x3 block constraints
block(1..3).
:- num(N), block(BR), block(BC),
   #count { R,C : sudoku(R,C,N), R > (BR-1)*3, R <= BR*3, C > (BC-1)*3, C <= BC*3 } != 1.

% Initial values
:- initial(R,C,N), sudoku(R,C,M), N != M.

#show sudoku/3.