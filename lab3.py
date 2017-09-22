"""
 I pledge my honor that I have abided by the Stevens Honor System
 
 By Tim Zheng 
 22 Sep 2017
"""


def change(money, coinSystem):
    """Given an amount of money and a list of coin types (coinSystem), return the least number of coins that makes up that amount of money"""
    if money == 0:
        return 0
    if coinSystem == []:
        return float("inf")
    if money < 0:
        return float("inf")
    use_it = 1 + change(money - coinSystem[0], coinSystem)
    lose_it = change(money, coinSystem[1:])
    return min(use_it, float("inf") if lose_it == 0 else lose_it)


# def change1(money, coinSystem):
#     if money == 0:
#         return 0
#     if money < 0:
#         return 10000
#     return min(1 + change1(money - coinSystem[0], coinSystem), change1(money, coinSystem[1:]))


# print(change1(72, [1, 5, 10, 20, 50, 100]))







