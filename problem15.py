#!/usr/bin/env python

# Cornes have (2 1) choices, there are 4 corners.
# All non corner edges have tree choices, 4 * (side - 2)
# Choices inside the grid are (4 1), (side - 2) * (side - 2)

# 
# a 3x3 grid has :
#
# 4 corners 4 (2 1)
# 4 non corner edges, 4 (3 1)
# 1 inside grid square 1 (4 1)

# combinatorics for board
#
# (n over k ) => n! / k!(n - k)
#
# 2 over 1 => 2*1 / 1*(2 - 1) = 2 / 1 = 2
# 3 over 1 => 1*2*3 / 1*(3 - 1) = 6 / 2 = 3
# 4 over 1 => 1*2*3*4 / 1*(4 - 1) = 24 / 3 = 8

# choices for 3x3 grid:
#
# 4 corners
# 4 * (3 - 2) = 4 non corner edges
# (3 - 2) * (3 - 2) = 1 * 1 = 1 inside grid

# 4 * 2 + 4 * 3 + 1 * 8 = 8 + 12 + 8 = 28

# choices for a 20 x 20 grid:
#
# 4 corners
# 4 * (20 - 2) = 72 non corner edges
# (20 - 2) * (20 - 2) = 324 inside grid

# 4 * 2 + 72 * 3 + 324 * 8 = 2816
