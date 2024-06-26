% Define facts about fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(lemon, yellow).
fruit_color(cherry, red).
fruit_color(blueberry, blue).
fruit_color(plum, purple).
fruit_color(watermelon, green).
fruit_color(strawberry, red).

% Define a rule to find the color of a fruit
find_color(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Example queries:
% ?- find_color(apple, Color).
% ?- find_color(banana, Color).

% Define a rule to find all fruits of a specific color
find_fruits_of_color(Color, Fruit) :-
    fruit_color(Fruit, Color).

% Example queries:
% ?- find_fruits_of_color(red, Fruit).
% ?- find_fruits_of_color(yellow, Fruit).
