import math
from os import remove
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
"""def main():
    pass_ = input("Enter the new Password: ")
    if len(pass_)<8:
        print("Password must have at least 8 characters")
    else:
        pass_again = input("Reenter new Password: ")
        capital = 0
        lower = 0
        number = 0
        if pass_ == pass_again:
            for i in pass_:
                if i.isupper():
                    capital += 1
                    # print(capital)
                if i.islower():
                    lower += 1
                    # print(lower)
                if i.isnumeric():
                    number += 1
                    # print(number)
            if number == 0 or lower == 0 or capital == 0:
                print("Password not complex enough ")
            else:
                print("Password changed Successfully ")
        else:
            print("Passwords must match")

main()"""
"""class Solution:
    def twoSum(nums, target):
        # def listcheck(num, value):
        #     for i in num:
        #         if
        for o in range(99):
            if max(nums)>target:
                nums.remove(max(nums))
                continue
            elif max(nums)==target:
                return list(nums.index(max(nums)))
            else:
                for i in nums:
                    total = 0
                    rem = target - i
                    number = nums.count(rem)
                    if number == 1:
                        return_list = list()
                        return_list.append(nums.index(i))
                        return_list.append(nums.index(rem))
                        return return_list
                    else:
                        break


xx = Solution.twoSum([5,5], 10)
print(xx)"""
"""G = nx.Graph()

# Add 19 nodes
G.add_nodes_from(range(19))

# Attempt to add edges to make each vertex have degree 9
# Trying to manually connect vertices in a pattern that would give degree 9
edges = [
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9),
    (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
    (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11),
    (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12),
    (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13),
    (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14),
    (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15),
    (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (7, 16),
    (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (8, 16), (8, 17),
    (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 16), (9, 17), (9, 18),
    # Continue adding edges to try to ensure degree 9 for each vertex
    (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16), (10, 17), (10, 18),
    (11, 12), (11, 13), (11, 14), (11, 15), (11, 16), (11, 17), (11, 18),
    (12, 13), (12, 14), (12, 15), (12, 16), (12, 17), (12, 18),
    (13, 14), (13, 15), (13, 16), (13, 17), (13, 18),
    (14, 15), (14, 16), (14, 17), (14, 18),
    (15, 16), (15, 17), (15, 18),
    (16, 17), (16, 18),
    (17, 18)
]

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(8, 8))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')
plt.show()
"""
"""sum = 0
n=5
for i in range(n):
    sum += 2*i
print(sum)"""
"""fltstr = "1.0,20.0,1.24"

lst = []
a, b= fltstr.split(",", maxsplit=1)
lst.append(float(a))
b
print(a,b, sep="\n")"""
"""
items = [3, 1, 4, 2, ""]
a = 0
b = 0
c = ""
for i in items:
    if type(i) == int:
        if i > a:
            a = i
        else:
            continue
    elif type(i) == float:
        if i > b:
            b = i
        else:
            continue
    elif type(i) == str:
        if i > "":
            c = i
        else:
            continue
if a == 0:
    a = None
if b == 0:
    b = None
if c == "":
    c = None

print((a, b, c))"""
"""x = int(input("Enter the number: "))
if type(x) != int:
    print("Entered Value is not a number")
else:
    if x < 1:
        print("N must be greater than 1")
    elif x > 100:
        print("Too much work, no thanks")
    else:
        for i in range(1, x + 1):
            if i % 3 == 0 and i % 5 != 0:
                print("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            else:
                print(i)"""
"""def maxbytype(items):
    '''
    Assume that parameter 'items' is a heterogeneous list that
    may contain integers, floats, strings, and any other type.

    You should return a 3-tuple, where the first element is the
    largest integer, the second element is the largest float,
    and the third element is the largest string.

    If any of the types are not found in the list at all, there
    can logically be no maximum, and therefore you should use
    the value None to represent this.

    Example #1) if the input list is:
    [ "hello", 1, 3.14, 99, "cat", "tac", 2.7, "bat" ]
    Then the tuple returned should be: (99, 3.14, "tac")

    Example #2) if the input list is:
    [ "hello", 1, 99, "cat", "tac", "bat" ]
    Then the tuple returned should be: (99, None, "tac")

    You can check the type of any object in Python by using the
    type() function. For example, type(item) == float, will
    return True if item is a float, False otherwise.

    FOOD FOR THOUGHT:
    Why might we use the special value 'None' when there is no
    instance of a particular type present in the list? Why not
    use some error value, eg. -1 for integers, or the empty
    string if there is no string?

    '''
    a_l = []
    b_l = []
    c_l = []
    for i in items:
        if type(i) == int:
            a_l.append(i)
        elif type(i) == float:
            b_l.append(i)
        elif type(i) == str:
            c_l.append(i)
    if len(a_l) == 0:
        a = None
    else:
        a = max(a_l)
    if len(b_l) == 0:
        b = None
    else:
        b = max(b_l)
    if len(c_l) == 0:
        c = None
    else:
        c = max(c_l)
    return (a, b, c)

print(maxbytype([0,"apple",9.7, 10.26, "zebra", True]))
"""
"""
def paritypartition(items):

    '''
    This function accepts a list of integers, and returns a list
    containing the exact same integers, but separated by even
    and odd. All the even numbers should be at the front of the
    list, and all the odd numbers should be at the back.

    The relative order of the even numbers should be the same
    as the original list. The same applies to the odd numbers.

    For example, given the input list:  [7, 0, 4, -1, 3, 2, 1]
    this function should return:        [0, 4, 2, 7, -1, 3, 1]

    '''

    even, odd = [], []
    for i in items:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    even.sort()
    odd.sort()
    fin = even + odd
    return fin
print(paritypartition([7, 0, 4, -1, 3, 2, 1]))"""
"""
def domninocycle(tiles):

    '''
    This is another from Ilkka's problem set.

    A single domino tile is represented as a two-tuple of its
    pip values, such as (2,5) or (6,6). This function should
    determine whether the given list of tiles forms a cycle so
    that each tile in the list ends with the exact same pip value
    that its successor tile starts with, the successor of the
    last tile being the first tile of the list since this is
    supposed to be a cycle instead of a chain.

    Return True if the given list of tiles forms such a cycle,
    and False otherwise.

    For example, for the input  [(3, 5), (5, 2), (2, 3)], this
    function should return True.

    For the input [(2, 5), (5, 2), (2, 3)], this function
    returns False because the first value on the first tile (2)
    does not match the 2nd value on the last tile (3)

    '''


    if tiles[0][0] != tiles[-1][0]:
        print(tiles[0][0])
        print(tiles[-1][0])
        return True
    for i in range(len(tiles)-1):
        if tiles[i][1] != tiles[i+1][0]:
            return False
    return False
domninocycle([(3, 5), (5, 2), (2, 3)])
"""
"""
def login():
    currently_checked_in = []
    while True:
        user_input = input()
        if user_input == "check in":
            name = input("What is your name? ")
            currently_checked_in.append(name)
        elif user_input == "check out":
            name = input("What is your name? ")
            currently_checked_in.remove(name)
        elif user_input == "who":
            for i in currently_checked_in:
                print(i, end=", ")
            print()
        elif user_input == "end":
            print("bye bye")
            break
        else:
            print("Invalid input")

login()
"""
"""
def faro(lst, bol):
    x = len(lst)
    if x == 0:
        return []
    x = int(x/2)
    incoming = lst[:x]
    outgoing = lst[x:]
    if bol == "True":
        fin = []
        for i in range(len(incoming)):
            fin.append(incoming[i])
            fin.append(outgoing[i])
        return fin
    elif bol == "False":
        fin = []
        for i in range(len(incoming)):
            fin.append(outgoing[i])
            fin.append(incoming[i])
    return fin

lst = eval(input("list: " ))
bol = input("bol: " )
print(faro(list(lst), bol))
"""
"""
def is_prime(num):
    if num == 0 or num == 1:
        return "not prime"
    x = list(range(2, num))
    if any(num%(x)==0 for x in x):
        return "not prime"
    else: return "is prime"

x=int(input("number: "))
print(is_prime(x))
"""
"""
mass = 800  # kg
initial_speed = 4.0  # m/s
final_speed = 4.28  # m/s
force_you = np.array([-400, 400, 300])  # N
initial_position = np.array([3.9, -1.3, 2.4])  # m
final_position = np.array([2.9, 2.3, -11.4])  # m

# Recalculate displacement vector
displacement = final_position - initial_position

# Recalculate work done by "you"
work_you = np.dot(force_you, displacement)

# Recalculate change in kinetic energy (ΔKE)
delta_ke = 0.5 * mass * (final_speed**2 - initial_speed**2)

# Recalculate work done by friend
work_friend = delta_ke - work_you
print(work_friend)
"""
"""
# Make a function that reverses a list
def list_reverse(items):
    try:
        if type(items[0]) == list:
            return list_reverse(items[1:])+[list_reverse(items[0])]
        else:
            return list_reverse(items[1:])+[items[0]]
    except IndexError:
        return items
print(list_reverse([3,5,[1,2],8,0]))
""" #**
"""def next_item(it):
    try:
        return next(it) if type(next(it))==int else None
    except StopIteration:
        return None

it = [1,'cat', 1, 4]
it = iter(it)
print(next_item(it))
print(next_item(it))
print(next_item(it))
print(next_item(it))
print(next_item(it))
print(next_item(it))
"""
n = [1,4,6,2,5,7]
print(n[1:-1])