# 1) return a list of all students whose firstName begins with the character letter
def get_students_starting_with(students, letter):
    pass
    # example: get_students_starting_with(['Tanguy', 'Amine'], 'a') => ['Amine']


# 2) return the result obtained by student if:

# 2.a) you know its position in the results list
def get_score_position(results, index):
    pass
    # example: get_score_position([["Tanguy", 5], ["Amine", 7]], 0) => 5


# 2.b) you don't know its position in the results list
def get_score_unknown_position(results, name):
    pass
    # example: get_score_unknown_position([["Tanguy", 5], ["Amine", 7]], 'Amine') => 7


# 3) return an average of the mathematics's result of all students (suppose you don't know the list's length)
def average_math_result(results):
    pass
    # example: get_average_math_result([["Tanguy", 5], ["Amine", 7]]) => 6


# 4) return a new list with all students who succeeded (>= 50%) mathematics
def student_who_succeeded(results):
    pass
    # example: student_who_succeeded([["Tanguy", 5], ["Amine", 7]]) => ['Tanguy', 'Amine']


# 5) return a new list with all student that didn't participate to the mathematics's exam
def not_participating(students, results):
    pass
    # example: not_participating(['Tanguy', 'Amine'], [["Tanguy", 5]]) => ['Amine']
