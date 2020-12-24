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
def the_winner_is(n, total_of_cals=0):
    """this function calculates who would win in a Nim game,
    when both players play an optimal game. in addition, it
    calculate the number of recursion calls"""
    # total_of_cals default is 0
    total_of_cals = total_of_cals
    # if we got to the situation where n == 0, it means that the first
    # player loosed.
    if n == 0:
        print("Player 1 lose with {} calls".format(total_of_cals))
        return False
    # since the rule of the game is that in any turn a player can take
    # one, or two or four coins, in these situations the player will win,
    # and live an empty board
    elif n == 1 or n == 2 or n == 4:
        print("Player 1 won with {} calls".format(total_of_cals))
        return True
    else:
        # we will simplified the game using recursion, now with -3 coins
        total_of_cals += 1
        return the_winner_is(abs(n - 3), total_of_cals)


def coin_pick_winner(n):
    first_step = the_winner_is(n)
    if n >= 9:
        if n % 3 == 0:
            return first_step, 3
        elif n % 3 == 1:
            return first_step, 2
        else:
            return first_step, 1
    elif n < 9 and n != 3 and n != 4:
        return first_step, 1
    else:
        return first_step, 2
