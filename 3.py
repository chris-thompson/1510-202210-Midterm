"""
FUNCTION:
_________

Define a function called validate_lo_shu that accepts a 2D list as an argument.

The 2D list may represent a Lo Shu Magic Square of ANY SQUARE SIZE.

The function must return True if the list is a Lo Shu Magic Square of ANY SQUARE SIZE.

The function must return False if the argument is anything else.

You may not modify the 2D list passed as an argument in any way, even temporarily.

DESCRIPTION:
____________

The Lo Shu Magic Square is a square matrix of positive integers.

The Lo Shu Magic Square has the following two properties:
i.  The numbers in the grid are unique
ii. The sum of each row, column, and each diagonal is the same number.

Here are some examples...

In this 4 x 4 (order 4) Lo Shu Magic Square, the sum is 34:

16   2   3  13
 5  11  10   8
 9   7   6  12
 4  14  15   1

In this 5 x 5 (order 5) Lo Shu Magic Square, the sum is 65:

22  18   3   2  20
 7  16   9  14  19
 5  11  13  15  21
25  12  17  10   1
 6   8  23  24   4

In this 6 x 6 (order 6) Lo Shu Magic Square, the sum is 111:

32 29  4  1 24 21
30 31  2  3 22 23
12  9 17 20 28 25
10 11 18 19 26 27
13 16 36 33  5  8
14 15 34 35  6  7

DOCSTRING:
__________

YES. Full docstrings are needed. Include pre- and post-conditions.

DOCTESTS:
_________

You must create TWO (2) useful doctests for this function to show me that it
correctly identifies Lo Shu Magic Squares of different sizes. You must also add ONE (1)
doctest that shows me than a square matrix that is NOT a Lo Shu Magic Square will,
when passed to the function, generate a False return value.

"""
