% Facts
% student(StudentName, TeacherName, SubjectCode).
student('Alice', 'Mr. Smith', 'MATH101').
student('Bob', 'Ms. Johnson', 'ENG202').
student('Charlie', 'Mr. Smith', 'SCI303').
student('David', 'Ms. Johnson', 'MATH101').
student('Eva', 'Mr. Brown', 'HIST404').

% Rules
% Get all students
all_students(StudentName, TeacherName, SubjectCode) :- student(StudentName, TeacherName, SubjectCode).

% Find students by teacher
find_students_by_teacher(TeacherName, StudentName, SubjectCode) :- student(StudentName, TeacherName, SubjectCode).

% Find students by subject code
find_students_by_subject(SubjectCode, StudentName, TeacherName) :- student(StudentName, TeacherName, SubjectCode).

% Find teachers by student
find_teachers_by_student(StudentName, TeacherName, SubjectCode) :- student(StudentName, TeacherName, SubjectCode).

% Example Queries
% ?- all_students(StudentName, TeacherName, SubjectCode).
% ?- find_students_by_teacher('Mr. Smith', StudentName, SubjectCode).
% ?- find_students_by_subject('MATH101', StudentName, TeacherName).
% ?- find_teachers_by_student('Alice', TeacherName, SubjectCode).
