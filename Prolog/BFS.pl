:- use_module(library(lists)). % For list operations

% Define edges with costs
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 1).
edge(b, e, 6).
edge(c, f, 2).
edge(d, g, 1).
edge(e, g, 2).
edge(f, g, 4).

% Define heuristic values (estimated cost to reach goal)
heuristic(a, 4).
heuristic(b, 2).
heuristic(c, 4).
heuristic(d, 1).
heuristic(e, 2).
heuristic(f, 2).
heuristic(g, 0). % Goal node

% Best-First Search
best_first_search(Start, Goal, Path) :-
    heuristic(Start, H),
    best_first_search([[Start, 0, H]], Goal, [], Path).

best_first_search([[Goal, _, _] | _], Goal, Visited, Path) :-
    reverse([Goal | Visited], Path).

best_first_search([[Node, Cost, _] | Rest], Goal, Visited, Path) :-
    findall(
        [NextNode, NewCost, H],
        (
            edge(Node, NextNode, StepCost),
            \+ member(NextNode, Visited),
            NewCost is Cost + StepCost,
            heuristic(NextNode, H)
        ),
        Neighbors
    ),
    append(Rest, Neighbors, OpenList),
    sort_by_heuristic(OpenList, SortedOpenList),
    best_first_search(SortedOpenList, Goal, [Node | Visited], Path).

% Sort list of nodes by heuristic value
sort_by_heuristic(Unsorted, Sorted) :-
    map_list_to_pairs(get_heuristic, Unsorted, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

get_heuristic([_, _, H], H).

% Helper predicates for debugging and displaying the path
print_path([]).
print_path([Node | Rest]) :-
    write(Node), nl,
    print_path(Rest).

% Example usage
solve(Start, Goal) :-
    best_first_search(Start, Goal, Path),
    write('Path found: '), nl,
    print_path(Path).



