% Define diseases and their symptoms
disease(cold) :- has_symptom(fever), has_symptom(cough), has_symptom(sore_throat).
disease(flu) :- has_symptom(fever), has_symptom(cough), has_symptom(headache), has_symptom(body_ache).
disease(covid19) :- has_symptom(fever), has_symptom(cough), has_symptom(shortness_of_breath), has_symptom(loss_of_taste_or_smell).
disease(strep_throat) :- has_symptom(sore_throat), has_symptom(fever), has_symptom(swollen_lymph_nodes).
disease(allergy) :- has_symptom(sneezing), has_symptom(runny_nose), has_symptom(watery_eyes).

% Define symptoms
symptom(fever).
symptom(cough).
symptom(sore_throat).
symptom(headache).
symptom(body_ache).
symptom(shortness_of_breath).
symptom(loss_of_taste_or_smell).
symptom(swollen_lymph_nodes).
symptom(sneezing).
symptom(runny_nose).
symptom(watery_eyes).

% Define the rules to check for symptoms
has_symptom(Symptom) :- symptom(Symptom), write('Do you have '), write(Symptom), write('? (yes/no)'), nl, read(Reply), Reply = yes.

% Diagnose the disease based on symptoms
diagnose(Disease) :-
    disease(Disease), !.

% Main predicate to start the diagnosis
start_diagnosis :-
    write('Welcome to the medical diagnosis system!'), nl,
    write('Please answer the following questions:'), nl,
    ( diagnose(Disease) ->
        write('Based on the symptoms, you might have '), write(Disease), write('.'), nl;
        write('Sorry, we could not diagnose your illness based on the provided symptoms.'), nl
    ).

% Example usage:
% ?- start_diagnosis.
