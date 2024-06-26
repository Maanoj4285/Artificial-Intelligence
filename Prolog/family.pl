% Define family relationships
% male(Name)
male(john).
male(paul).
male(mike).
male(tom).
male(jim).

% female(Name)
female(linda).
female(mary).
female(susan).
female(kate).
female(ann).

% parent(Parent, Child)
parent(john, paul).
parent(john, mary).
parent(linda, paul).
parent(linda, mary).
parent(paul, mike).
parent(susan, mike).
parent(mary, kate).
parent(tom, kate).
parent(kate, ann).
parent(jim, ann).

% Rules to infer additional relationships

% father(Father, Child)
father(F, C) :-
    male(F),
    parent(F, C).

% mother(Mother, Child)
mother(M, C) :-
    female(M),
    parent(M, C).

% child(Child, Parent)
child(C, P) :-
    parent(P, C).

% sibling(Sibling1, Sibling2)
sibling(S1, S2) :-
    parent(P, S1),
    parent(P, S2),
    S1 \= S2.

% brother(Brother, Sibling)
brother(B, S) :-
    male(B),
    sibling(B, S).

% sister(Sister, Sibling)
sister(S, Sibling) :-
    female(S),
    sibling(S, Sibling).

% grandparent(Grandparent, Grandchild)
grandparent(GP, GC) :-
    parent(GP, P),
    parent(P, GC).

% grandfather(Grandfather, Grandchild)
grandfather(GF, GC) :-
    male(GF),
    grandparent(GF, GC).

% grandmother(Grandmother, Grandchild)
grandmother(GM, GC) :-
    female(GM),
    grandparent(GM, GC).

% grandchild(Grandchild, Grandparent)
grandchild(GC, GP) :-
    grandparent(GP, GC).

% uncle(Uncle, NieceOrNephew)
uncle(U, N) :-
    male(U),
    sibling(U, P),
    parent(P, N).

% aunt(Aunt, NieceOrNephew)
aunt(A, N) :-
    female(A),
    sibling(A, P),
    parent(P, N).

% nephew(Nephew, UncleOrAunt)
nephew(N, UorA) :-
    male(N),
    sibling(UorA, P),
    parent(P, N).

% niece(Niece, UncleOrAunt)
niece(N, UorA) :-
    female(N),
    sibling(UorA, P),
    parent(P, N).

% cousin(Cousin1, Cousin2)
cousin(C1, C2) :-
    parent(P1, C1),
    parent(P2, C2),
    sibling(P1, P2).

