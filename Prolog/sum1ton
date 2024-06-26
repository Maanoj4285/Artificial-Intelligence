% sum_to_n(N, Sum) computes the sum of numbers from 1 to N.
sum_to_n(0, 0).  % Base case: The sum of numbers from 1 to 0 is 0.
sum_to_n(N, Sum) :-
    N > 0,                  % Ensure N is positive.
    N1 is N - 1,            % Decrease N by 1.
    sum_to_n(N1, Sum1),     % Recursively find the sum of numbers from 1 to N-1.
    Sum is N + Sum1.        % Sum is the current number N plus the sum of numbers from 1 to N-1.
