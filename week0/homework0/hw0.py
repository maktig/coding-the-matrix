# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [ i for i in L if i % num != 0 ]



## Problem 2
def myLists(L): return [ list(range(1,i+1)) for i in L ]



## Problem 3
def myFunctionComposition(f, g):
    mydict = {}
    for k,v in f.items():
        mydict[k] = g[v]

    return mydict

## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j
complex_addition_b = 1j
complex_addition_c = -1 + .001j
complex_addition_d = .001 + 9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    n = 0
    for i in L:
        n += i
    return n



## Problem 7
def myProduct(L):
    n = 1
    for i in L:
        n *= i
    return n


## Problem 8
def myMin(L):
    n = float('Inf')
    for i in L:
        if i < n:
            n = i
    return n



## Problem 9
def myConcat(L):
    current = ""
    for i in L:
        current += i
    return current



## Problem 10
def myUnion(L):
    current = set()
    for i in L:
        for j in i:
            current.add(j)
    return current

