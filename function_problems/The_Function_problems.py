# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1) Tuple Sum
def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    '''
    return [(x1 + y1, x2 + y2) for (x1, x2), (y1, y2) in zip(A, B)]



## 2: (Problem 2) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Examples:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'})
    {'merci':'thank you', 'au revoir':'goodbye'}]
    '''
    return {v:k for k,v in d.items()}



## 3: (Problem 3) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    return [p+i for i,p in enumerate([p]*n)]

comprehension_with_row = [row(x, 20) for x in range(15)]

comprehension_without_row = [[i+p for i,p in enumerate([x]*20)] for x in range(15)]



## 4: (Problem 4) Probability Exercise 1
Pr_dict = {1: 0.5, 2: 0.2, 3: 0.1, 5: 0.1, 6: 0.1}
f = {x: x + 1 for x in range(1,7)}
Pr_f_is_even = sum([Pr_dict.get(k, 0) for k in range(1,7) if f[k] % 2 == 0])
Pr_f_is_odd  = sum([Pr_dict.get(k, 0) for k in range(1,7) if f[k] % 2 != 0])



## 5: (Problem 5) Probability Exercise 2
g = {k: k % 3 for k in range(1, 8)}
Pr_g = {1: 0.2, 2: 0.2, 3: 0.2, 4: 0.1, 5: 0.1, 6: 0.1, 7: 0.1}
Pr_g_is_1 = sum([Pr_g[k] for k, v in g.items() if v == 1])
Pr_g_is_0or2 = sum([Pr_g[k] for k, v in g.items() if v != 1])

