% Move N disks from Source peg to Destination peg using Auxiliary peg
hanoi(0, _, _, _) :- !.
hanoi(N, Source, Destination, Auxiliary) :-
    N > 0,
    M is N - 1,
    hanoi(M, Source, Auxiliary, Destination),
    move(Source, Destination),
    hanoi(M, Auxiliary, Destination, Source).

% Define the move action
move(Source, Destination) :-
    write('Move disk from '), write(Source), write(' to '), write(Destination), nl.

% Example query to solve the problem for 3 disks
% ?- hanoi(3, 'A', 'C', 'B').
