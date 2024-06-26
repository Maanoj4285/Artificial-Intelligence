% Facts
bird(penguin).
bird(sparrow).
bird(eagle).
flies(sparrow).
flies(eagle).
aquatic(penguin).

% Rules for forward chaining
can_fly(X) :- bird(X), flies(X).
can_swim(X) :- bird(X), aquatic(X).

% Forward chaining inference
infer_properties :-
    findall(X, bird(X), Birds),
    process_birds(Birds).

process_birds([]).
process_birds([Bird|Rest]) :-
    (   can_fly(Bird) -> assert(fly_ability(Bird))
    ;   true
    ),
    (   can_swim(Bird) -> assert(swim_ability(Bird))
    ;   true
    ),
    process_birds(Rest).

% Backward chaining rules and queries
can_do_action(X, fly) :- bird(X), flies(X).
can_do_action(X, swim) :- bird(X), aquatic(X).

query_can_fly(X) :-
    can_do_action(X, fly),
    format('~w can fly.~n', [X]).

query_can_swim(X) :-
    can_do_action(X, swim),
    format('~w can swim.~n', [X]).


