% Facts
% planet(Name, Type, DistanceFromSun, NumberOfMoons).
planet('Mercury', terrestrial, 57.9, 0).
planet('Venus', terrestrial, 108.2, 0).
planet('Earth', terrestrial, 149.6, 1).
planet('Mars', terrestrial, 227.9, 2).
planet('Jupiter', gas_giant, 778.3, 79).
planet('Saturn', gas_giant, 1427.0, 82).
planet('Uranus', ice_giant, 2871.0, 27).
planet('Neptune', ice_giant, 4497.1, 14).

% Rules
% Get all planets
all_planets(Name, Type, DistanceFromSun, NumberOfMoons) :-
    planet(Name, Type, DistanceFromSun, NumberOfMoons).

% Find planets by type
find_planets_by_type(Type, Name, DistanceFromSun, NumberOfMoons) :-
    planet(Name, Type, DistanceFromSun, NumberOfMoons).

% Find planets by distance from the sun (less than a given distance)
find_planets_by_distance(MaxDistance, Name, Type, DistanceFromSun, NumberOfMoons) :-
    planet(Name, Type, DistanceFromSun, NumberOfMoons),
    DistanceFromSun =< MaxDistance.

% Find planets by number of moons (greater than a given number)
find_planets_by_moons(MinMoons, Name, Type, DistanceFromSun, NumberOfMoons) :-
    planet(Name, Type, DistanceFromSun, NumberOfMoons),
    NumberOfMoons >= MinMoons.

% Example Queries
% ?- all_planets(Name, Type, DistanceFromSun, NumberOfMoons).
% ?- find_planets_by_type(terrestrial, Name, DistanceFromSun, NumberOfMoons).
% ?- find_planets_by_distance(1500, Name, Type, DistanceFromSun, NumberOfMoons).
% ?- find_planets_by_moons(10, Name, Type, DistanceFromSun, NumberOfMoons).
