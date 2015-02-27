# version code 122ffbc9f6c3+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Be sure that the file voting_record_dump109.txt is in the matrix/ directory.





## 1: (Task 2.12.1) Create Voting Dict
def create_voting_dict(strlist):
    """
    Input: a list of strings.  Each string represents the voting record of a senator.
           The string consists of 
              - the senator's last name, 
              - a letter indicating the senator's party,
              - a couple of letters indicating the senator's home state, and
              - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                votes on bills
              all separated by spaces.
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting record.
    Example: 
        >>> vd = create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
        >>> vd == {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}
        True

    You can use the .split() method to split each string in the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.

    You can use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    The lists for each senator should preserve the order listed in voting data.
    In case you're feeling clever, this can be done in one line.
    """
    entries = {}
    for s in [str.split(i) for i in strlist]:
        entries[s[0]] = [int(i) for i in s[3:]]
    return entries


## 2: (Task 2.12.2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    
    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253
        
    You should definitely try to write this in one line.
    """
    return sum([i*j for i,j in zip(voting_dict[sen_a], voting_dict[sen_b])])



## 3: (Task 2.12.3) Most Similar
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    similar = ''
    similar_score = -float("inf")
    for other_sen in [e for e in voting_dict.keys() if e != sen]:
        score = policy_compare(sen, other_sen, voting_dict)
        if score > similar_score:
            similar = other_sen
            similar_score = score
    return similar



## 4: (Task 2.12.4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
    """
    similar = ''
    similar_score = float("inf")
    for other_sen in [e for e in voting_dict.keys() if e != sen]:
        score = policy_compare(sen, other_sen, voting_dict)
        if score < similar_score:
            similar = other_sen
            similar_score = score
    return similar



## 5: (Task 2.12.5) Chafee, Santorum
voting_dict = create_voting_dict(list(open('voting_record_dump109.txt')))
most_like_chafee    = most_similar("Chafee", voting_dict)
least_like_santorum = least_similar("Santorum", voting_dict)

## Ungraded task
senators_by_states = {}
for entries in [str.split(s) for s in list(open('voting_record_dump109.txt'))]:
    senators_by_states.setdefault(entries[2], []).append(entries[0])
senators_for_TX = senators_by_states['TX'];
favorite_state_senator_similarity = policy_compare(senators_for_TX[0], senators_for_TX[1], voting_dict)


## 6: (Task 2.12.7) Most Average Democrat
def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    return sum([policy_compare(sen, other_sen, voting_dict) for other_sen in sen_set])/len(sen_set)

## gather senators by party
senators_by_party = {}
for entries in [str.split(s) for s in list(open('voting_record_dump109.txt'))]:
    senators_by_party.setdefault(entries[1], []).append(entries[0])
democrats = senators_by_party['D']

most_average_Democrat = max(voting_dict.keys(), key=lambda d:find_average_similarity(d, democrats, voting_dict)) # give the last name (or code that computes the last name)



## 7: (Task 2.12.8) Average Record
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
        >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
        >>> find_average_record({'a','c','e'}, d)
        [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
        >>> find_average_record({'a','c','e','b'}, d)
        [-0.5, 0.0, 0.75]
        >>> find_average_record({'a'}, d)
        [0.0, 1.0, 1.0]
    """
    return [float(sum(x))/len(x) for x in zip(*[voting_dict[k] for k in sen_set])]

#voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
#find_average_record({'Fox-Epstein','Ravella'}, voting_dict)

average_Democrat_record = find_average_record(democrats, voting_dict)



## 8: (Task 2.12.9) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Ravella') or br == ('Ravella', 'Fox-Epstein')
        True
    """
    lhs_worse = None
    rhs_worse = None
    value = float('inf')
    for i, sen_a in enumerate(voting_dict.keys()):
        for j, sen_b in enumerate(voting_dict.keys()):
            if i < j:
                v = policy_compare(sen_a, sen_b, voting_dict)
                if v < value:
                    lhs_worse = sen_a
                    rhs_worse = sen_b
                    value = v

    return (lhs_worse, rhs_worse)
            

# voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
# br = bitter_rivals(voting_dict)
# br == ('Fox-Epstein', 'Ravella') or br == ('Ravella', 'Fox-Epstein')
