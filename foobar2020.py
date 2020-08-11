# Problem statement:
#
# Write a function solution(w, h, s) that takes 3 integers and returns the number of unique, non-equivalent configurations that can be found on a star grid w blocks wide and h blocks tall where each celestial body has s possible states. Equivalency is defined as above: any two star grids with each celestial body in the same state where the actual order of the rows and columns do not matter (and can thus be freely swapped around). Star grid standardization means that the width and height of the grid will always be between 1 and 12, inclusive. And while there are a variety of celestial bodies in each grid, the number of states of those bodies is between 2 and 20, inclusive. The solution can be over 20 digits long, so return it as a decimal string.  The intermediate values can also be large, so you will likely need to use at least 64-bit integers.
# 
# For example, consider w=2, h=2, s=2. We have a 2x2 grid where each celestial body is either in state 0 (for instance, silent) or state 1 (for instance, noisy).  We can examine which grids are equivalent by swapping rows and columns.
# 
# 00
# 00
# 
# In the above configuration, all celestial bodies are "silent" - that is, they have a state of 0 - so any swap of row or column would keep it in the same state.
# 
# 00 00 01 10
# 01 10 00 00
# 
# 1 celestial body is emitting noise - that is, has a state of 1 - so swapping rows and columns can put it in any of the 4 positions.  All four of the above configurations are equivalent.
# 
# 00 11
# 11 00
# 
# 2 celestial bodies are emitting noise side-by-side.  Swapping columns leaves them unchanged, and swapping rows simply moves them between the top and bottom.  In both, the *groupings* are the same: one row with two bodies in state 0, one row with two bodies in state 1, and two columns with one of each state.
# 
# 01 10
# 01 10
# 
# 2 noisy celestial bodies adjacent vertically. This is symmetric to the side-by-side case, but it is different because there's no way to transpose the grid.
# 
# 01 10
# 10 01
# 
# 2 noisy celestial bodies diagonally.  Both have 2 rows and 2 columns that have one of each state, so they are equivalent to each other.
# 
# 01 10 11 11
# 11 11 01 10
# 
# 3 noisy celestial bodies, similar to the case where only one of four is noisy.
# 
# 11
# 11
# 
# 4 noisy celestial bodies.
# 
# There are 7 distinct, non-equivalent grids in total, so solution(2, 2, 2) would return 7.


def solution(w, h, s):
    # We can find the solution to the problem by applying Polya's Enumeration
    # Theorem: https://en.wikipedia.org/wiki/P%C3%B3lya_enumeration_theorem
    #
    # Let's give a simplified intro to the theorem:
    #
    # Let Y be a set of options and X the set of places those options can be in
    # (think of a bracelet with different coloured beads. The set of possible
    # colours are Y. The "index" of the beads {1, 2, 3, ..., n} for n beads
    # builds X.).
    # Then Y**X describes all possible bracelet arrangements.
    #
    # Let G be the set of all permutations of X that are considered symmetric
    # to one another (or equivalently all the symmetric group actions on X).
    # In our bead example this might be the set of all rotations of the
    # bracelet. For 3 beads it could look like this:
    # { {1, 2, 3}, {3, 1, 2}, {2, 3, 1} }
    #
    # Converting these permutations to cycles in their current order yields:
    # { (1)(2)(3),  # reads: 1 stays at 1, 2 stays at 2, 3 stays at 3
    #   (1, 2, 3),  # reads: 1 goes to 2, 2 goes to 3, 3 goes to 1
    #   (1, 3, 2) } # reads: 1 goes to 3, 3 goes to 2, 2 goes to 1
    # Generally, a permutation and its description in cycles are equivalent.
    # So, this set is the same as G.
    #
    # The number of cycles (=: c(S)) for each action in this notation is the
    # number of pairs of parentheses/cycles: so in our case c(G) =
    # { c( (1)(2)(3) ) = 3,
    #   c( (1, 2, 3) ) = 1,
    #   c( (1, 3, 2) ) = 1 }
    # = { 3, 1, 1}
    #
    # Furthermore, let Y**X / G be the set of all permutations of Y**X that
    # are unique under the symmetric actions, i.e. applying any symmetry action
    # to a permutation in Y**X does not yield any other element in Y**X.
    # In our bead example for a bracelet of length 3 with 2 bead colours (0/1),
    # Y**X / G looks like this:
    # { 000, 001, 011, 111 }
    # For example: 010 is not in the set as it can be obtained by rotating 001
    #
    # Polya then states:
    # The order (i.e. the number of elements in a set) of Y**X / G equals
    # 1/order(G) * sum( order(Y)**c(g) for each permutation g in G)
    #
    # let's apply it to our 3 bead example. As seen above Y**X / G has 4
    # elements. So 4 is the expected result:
    # 1/3 * sum( 2**3, 2**1, 2**1) = 1/3 * 12 = 4
    # Beautiful!
    #
    # Before we apply Polya theorem to our problem, let's have a look at the
    # cycle index polynomial of a group action:
    #
    # First, let c_i(g) be the number of cycles with a given length i in g.
    # For example: c_1( (1)(2, 3) ) = 1, # there is 1 cycle of length 1: (1)
    #              c_2( (1)(2, 3) ) = 1, # there is 1 cycle of length 2: (2, 3)
    #              c_3( (1)(2, 3) ) = 0  # there are 0 cycles of length 3
    #
    # Then, the cycle index (polynomial) Z(G, x_1, x_2, ... , x_n) equals
    # 1/order(G) * sum( product( (x_i)**c_i(g) for each cycle length i)
    #                   for each permutation g in G)
    #
    # Let's take our previous G as example:
    # G = { (1)(2)(3), (1, 2, 3), (1, 3, 2) } then:
    # Z = 1/3 * sum( (x_1)**3 , (x_3)**1, (x_1)**1)
    #
    # This form looks an aweful lot like the result we got from Polya.
    # Let order(Y) = y then:
    # Z(G, x_1=y, x_2=y, ... , x_n=y) equals
    # 1/3 * sum( 2**3, 2**1, 2**1) = 1/3 * 12 = 4
    #
    # Evaluating the polynomial for x_1..n = order(Y) yields the same result!
    # Using this we can rewrite Polyas theorem as:
    # order(Y**X / G) = Z(G, x_1=y, x_2=y, ... , x_n=y)
    #
    # Now, that we have laid the theoretical groundwork, let's apply it:
    #
    # X is the set of {1, 2, 3, ... , h} x {1, 2, 3, ... , w} or the set of
    # all matrix index pairs of an h x w matrix.
    # (Basically all elements of a matrix)
    # Y is the set of numbers {0, 1, 2, ..., s-1}.
    #
    # Then Y**X is the set of all possible h x w matrices with entries 0..s-1 .
    #
    # The symmetric actions on rows and columns are S_h and S_w respectively.
    # This can be easily seen as there are h! ways to swap 2 rows and
    # w! ways for columns.
    # Swapping being the symmetric actions as per problem statement.
    #
    # It follows for G then:
    # G = S_w x S_h
    #
    # Following this stackexchange thread:
    # https://mathematica.stackexchange.com/questions/137643/how-to-get-the-cycleindexpolynomial-of-direct-product-of-two-symmetric-groups
    # referencing this research paper:
    # https://www.sciencedirect.com/science/article/pii/0012365X9390015L
    # we can compute the cycle index of G.
    #
    # After that, the only thing we need to do is plug in s into our polynomial
    # and return the answer. Easy as that!

    # And this would have been the part where I implement it myself but while
    # googling for efficient ways to implement such operations in Python
    # without the use of non-standard libraries I stumbled upon the possible
    # origin for the problem:
    # https://math.stackexchange.com/questions/2056708/number-of-equivalence-classes-of-w-times-h-matrices-under-switching-rows-and
    # And would you look at that: it already providesa python solution. 
    # So let's use that one instead of implementing our own!

    return str(answer(w, h, s))

# Credit to @AwokeKnowing for the following code.
# Implementation taken from here:
# https://math.stackexchange.com/questions/2056708/number-of-equivalence-classes-of-w-times-h-matrices-under-switching-rows-and

from fractions import *
from copy import *


def expand(frac, terml):
    for term in terml:
        term[0] *= frac
    return terml


def multiplyTerm(sub, terml):
    terml = deepcopy(terml)
    for term in terml:
        alreadyIncluded = False
        for a in term[1]:    # term[1] is a list like [[1,1],[2,3]]  where the
            if a[0] == sub:  # first item is subscript and second the exponent
                alreadyIncluded = True
                a[1] += 1
                break
        if not alreadyIncluded:
            term[1].append([sub, 1])

    return terml


def add(termla, termlb):
    terml = termla + termlb

    # now combine any terms with same a's
    if len(terml) <= 1:
        return terml
    #print "t", terml
    for i in range(len(terml) - 1):
        for j in range(i + 1, len(terml)):
            #print "ij", i, j
            if set([(a[0], a[1]) for a in terml[i][1]]) == set([(b[0], b[1]) for b in terml[j][1]]):
                terml[i][0] = terml[i][0] + terml[j][0]
                terml[j][0] = Fraction(0, 1)

    return [term for term in terml if term[0] != Fraction(0, 1)]


def lcm(a, b):
    return abs(a * b) / gcd(a, b) if a and b else 0

pet_cycnn_cache = {}
def pet_cycleind_symm(n):
    global pet_cycnn_cache
    if n == 0:
        return [ [Fraction(1.0), []] ]

    if n in pet_cycnn_cache:
        #print "hit", n
        return pet_cycnn_cache[n]

    terml = []
    for l in range(1, n + 1):
        terml = add(terml, multiplyTerm(l,  pet_cycleind_symm(n - l)) )

    pet_cycnn_cache[n] = expand(Fraction(1, n), terml)
    return pet_cycnn_cache[n]


def pet_cycles_prodA(cyca, cycb):
    alist = []
    for ca in cyca:
        lena = ca[0]
        insta = ca[1]

        for cb in cycb:
            lenb = cb[0]
            instb = cb[1]

            vlcm = lcm(lena, lenb)
            alist.append([vlcm, (insta * instb * lena * lenb) / vlcm])

    #combine terms (this actually ends up being faster than if you don't)
    if len(alist) <= 1:
        return alist

    for i in range(len(alist) - 1):
        for j in range(i + 1, len(alist)):
            if alist[i][0] == alist[j][0] and alist[i][1] != -1:
                alist[i][1] += alist[j][1]
                alist[j][1] = -1

    return [a for a in alist if a[1] != -1]


def pet_cycleind_symmNM(n, m):
    indA = pet_cycleind_symm(n)
    indB = pet_cycleind_symm(m)
    #print "got ind", len(indA), len(indB), len(indA) * len(indB)
    terml = []

    for flatA in indA:
        for flatB in indB:
            newterml = [
                [flatA[0] * flatB[0], pet_cycles_prodA(flatA[1], flatB[1])]
            ]
            #print "b",len(terml)
            #terml = add(terml, newterml)
            terml.extend(newterml)

    #print "got nm"
    return terml


def substitute(term, v):
    total = 1
    for a in term[1]:
        #need to cast the v and a[1] to int or
        #they will be silently converted to double in python 3
        #causing answers to be wrong with larger inputs
        total *= int(v)**int(a[1])
    return (term[0] * total)


def answer(w, h, s):
    terml = pet_cycleind_symmNM(w, h)
    #print terml
    total = 0
    for term in terml:
        total += substitute(term, s)

    return int(total)


def test():
    result = solution(2, 3, 4)
    expected = str(430)
    print("Expected: {}, got: {}".format(expected, result))
    result = solution(2, 2, 2)
    expected = str(7)
    print("Expected: {}, got: {}".format(expected, result))


if __name__ == '__main__':
    test()
