# --------------------------------------------------------------
# CODING PROBLEMS: 
# --------------------------------------------------------------

'''

Fill in the functions below according to their descriptions. Test
your code by running the file "midterm_tests.py"

Make sure your code compiles before you finish the test, do NOT 
leave syntax errors in your code! This is VERY important.

You don't need to submit on D2L. Just save your code locally. Be
sure to fill in your full name and email below:

FULL NAME: <your name here>
TMU EMAIL: <your email here>

'''

# Q1) 
def roman_to_arabic(rn):
    '''
    rn is a string representing a roman numeral. Your program should convert
    this number to an arabic base-10 integer, and return it. Your function
    only has to work for first 10 roman numerals. If rn is not one of the first
    10 numerals, return None. The first 10 roman numerals are given below:

    I    = 1
    II   = 2
    III  = 3
    IV   = 4
    V    = 5
    VI   = 6
    VII  = 7
    VIII = 8
    IX   = 9
    X    = 10
    '''

    n = (("I",1),
         ("II",2),
         ("III",3),
         ("IV",4),
         ("V",5),
         ("VI",6),
         ("VII",7),
         ("VIII",8),
         ("IX",9),
         ("X",10))
    for i in range(len(n)):
        if n[i][0]==rn:
            return n[i][1]


# Q2)
def sum_even(n):
    '''
    Assume n is an integer >= 1.
    Return the sum of the integers, between 1-n inclusive, 
    that are even
    '''
    
    pass


# Q3)
def integers_exceed(n):
    '''
    How many consecutive integers, starting at 1, must be
    added before the sum exceeds n?
    For example, if n is 11, we must add 1+2+3+4+5 = 15,
    and therefore the answer is 5.
    '''

    sum = 0
    current = 1
    while sum<=n:
        sum += current
        current += 1
    if current == None:
        return 0
    return current-1


# Q4)
def leading_spaces(line):
    '''
    Assume that line is a string. Return the number of leading
    spaces in the string. Here, a 'space' refers to the space
    character. Not the newline, not the tab, just the space.
    '''
    
    pass


# Q5)
def first_letter(digits):
    '''
    Assume that digits is a string containing numeric digits.
    Returns a string whose corresponding characters are the first 
    letter of each digit.
    For example: '5113' returns 'foot',  since the first letters 
    of five, one, one, three are f, o, o, t.  
    Similarly, '0123456789613' returns 'zottffssensot'.
    '''

    pass


# Q6) 
def target_value(items, target):
    '''
    Assumes that items is a list, and target is any value.
    Return a new list containing only those elements in items that are 
    immediately followed by the target value.

    For example,
    ['value', 'key', 2, 3, 'key', 0], 'key' returns ['value', 3]
    [5, 3, 4], 7 returns []
    [7, 5, 3, 4], 7 returns []
    [7, 7, 7, 7], 7 returns [7, 7, 7]
    '''

    pass





        
