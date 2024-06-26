% Facts
bird(penguin).
bird(sparrow).
bird(eagle).
flies(sparrow).
flies(eagle).
aquatic(penguin).

% Rules
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

% Example queries
% Querying for capabilities inferred
query_inferred_capabilities :-
    write('Birds that can fly:'), nl,
    fly_ability(Bird),
    write(Bird), nl,
    fail.
query_inferred_capabilities :-
    write('Birds that can swim:'), nl,
    swim_ability(Bird),
    write(Bird), nl,
    fail.
query_inferred_capabilities.

% Example usage:
% To use, load the program and then execute `infer_properties.` to perform forward chaining.
% Afterward, query `query_inferred_capabilities.` to see the inferred capabilities.

% Example:
% ?- infer_properties.
% ?- query_inferred_capabilities.
