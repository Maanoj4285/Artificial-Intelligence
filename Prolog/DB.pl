% Facts
person('John Doe', '1990-01-01').
person('Jane Smith', '1985-05-15').
person('Alice Johnson', '1978-03-22').
person('Bob Brown', '2000-11-11').

% Get all people
all_people(Name, DOB) :- person(Name, DOB).

% Find a person by name
find_person_by_name(Name, DOB) :- person(Name, DOB).

% Find a person by date of birth
find_person_by_dob(DOB, Name) :- person(Name, DOB).
