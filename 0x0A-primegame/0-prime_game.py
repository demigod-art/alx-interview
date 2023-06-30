#!/usr/bin/python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def play_game(nums, is_maria_turn):
    if len(nums) == 0:
        return not is_maria_turn

    for i in range(len(nums)):
        if is_prime(nums[i]):
            new_nums = [num for num in nums if num % nums[i] != 0]
            if play_game(new_nums, not is_maria_turn) == is_maria_turn:
                return is_maria_turn
    
    return not is_maria_turn

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if play_game(list(range(1, num + 1)), True):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
