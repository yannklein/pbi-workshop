# Add a user to the tricount dictionary with a spent amount equals to 0
def add_user(tricount, user):
    pass


# Add an amount to the existing spent amount of a user
def add_amount(tricount, user, amount):
    pass


# Returns the amount spent by a user
def get_spent_amount(tricount, user):
    pass


# Returns the total of the spent amounts
def total_amount(tricount):
    pass


# Returns the due amount of a user
# This total is the sum of the spent amounts divided by the number of users minus the amount you already paid
# You balance may be negativ if you're owed money
def get_due_amount(tricount, user):
    pass


# Delete a user from the tricount without making any financial transfer
def delete(tricount, user):
    pass


# The function take the tricount dictionary and one of the user name as arguments
# It returns a dictionary with the amount due to each members by the user given as an argument
# Each amout due should be computed as follow: member spending / number of members
# It is a naive way to compute the amounts a user would need to reimbourse the others without the influence of what the user spent
# Example:
# tri_count_dic = {"Eric": 0.0, "Tanguy": 100.0, "Lucile": 0.0, 'Michael': 40.0}
# debts_dictionary(tri_count_dic, 'Lucile')
# => {"Eric": 0.0, "Tanguy": 25.0, 'Michael': 10.0}
def debts_dictionary(tricount, user):
    pass


# OPTIONAL
# Calculate what you owe to all other people, but this time you must consider the amount due by all users
# Example: Eric owes 10-5 = 5€ to Tanguy and Amine owes 10€ to Tanguy and 5€ to Eric in this situation Amine could give the total due to Tanguy
# The amount due of a user is the difference between his money spent and what he owes to the other user
# E.g.
# Input user = Amine and tricount = {'Eric': 15.0, 'Tanguy': 30.0, 'Amine': 0.0}
# Output {'Eric': 0.0, 'Tanguy': 15.0}
def final_owe(tricount, user):
    # Steps:
    # 1 - Compute total ratio of all user -> the difference between his money spent what the mean contribution expected by each user  
    # Input tricount = {'Eric': 12.0, 'Tanguy': 30.0, 'Amine': 0.0}
    # Output {'Eric': 2.0, 'Tanguy': -16.0, 'Amine': 14.0}
    # 2 - Allocate the transactions between the user and the other ones
    # Having a negativ sold obviously means that the user won't need to repay anyone, it's the easiest case
    # Then you need to distribute the due amounts:
    #     If some amounts are matching (e.g. -15 and 15) associate them, the goal is to reduce the number of transactions
    #         If the user's due amount matched, you've found your only transaction
    #         Else:
    #             You can either reimbourse several of the remaining solds if the user owes a lot
    #             Or partially reimbourse one of the biggest solds
    pass
