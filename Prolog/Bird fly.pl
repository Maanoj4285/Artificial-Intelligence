% Facts
% bird(Name, CanFly).
bird(sparrow, can_fly).
bird(penguin, cannot_fly).
bird(eagle, can_fly).
bird(ostrich, cannot_fly).
bird(parrot, can_fly).
bird(kiwi, cannot_fly).
bird(swallow, can_fly).
bird(flamingo, can_fly).

% Rules
% Determine if a bird can fly
can_fly(Bird) :- bird(Bird, can_fly).

% Determine if a bird cannot fly
cannot_fly(Bird) :- bird(Bird, cannot_fly).

% Example Queries
% ?- can_fly(sparrow).
% ?- cannot_fly(penguin).
% ?- can_fly(ostrich).
% ?- cannot_fly(kiwi).
