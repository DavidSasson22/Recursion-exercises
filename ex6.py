# 1
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


# 2
def is_palindrome(lst):
    if len(lst) < 1:
        return True
    if lst[0] == lst[-1]:
        return is_palindrome(lst[1:-1])
    return False


# 3
def sum_of_digits(n):
    if n // 10 == 0:
        return n
    return n % 10 + sum_of_digits(n // 10)


# 4
def convert_binary(n):
    if n <= 1:
        return str(n)
    return convert_binary(n // 2) + convert_binary(n % 2)


# 5
def nested_list_sum(lst):
    if type(lst) != list:
        return lst
    if not lst:
        return 0
    return nested_list_sum(lst[0]) + nested_list_sum(lst[1:])


# 6
def coin_pick_winner(n, total_of_cals=0):
    """this function calculates who would win in a Nim game, when both players
    play an optimal game. in addition, it calculate the number of recursion calls,
    and the number of possible optionsin the first step for winning, or for loosing
    if player B is the winner"""
    if n == 1 or n == 2:
        print("player 1 won: {} recursion calls were made".format(total_of_cals))
        # True means here that player 1 has one. the number represents the number of
        # possible steps at his first turn, for achieve his winning.
        return True, 1
    elif n == 3:
        return False, 2
    elif n == 4:
        return True, 2
    elif n == 6:
        return False, 3
    total_of_cals += 1
    return coin_pick_winner(n-3, total_of_cals)
