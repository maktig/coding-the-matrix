from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    mydict = {}
    for doc, words in enumerate(strlist):
        for w in words.split():
            if w in mydict.keys():
                mydict[w].add(doc)
            else:
                mydict[w] = {doc}

    return mydict

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    myset = set()
    for s in query:
        for w in s.split():
            if w in inverseIndex:
                docs = list(inverseIndex[w])
                for d in docs:
                    myset.add(d)
    return myset

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    words = [ w for s in query for w in s.split() ]
    mylist = list()
    for w in words:
        if w in inverseIndex:
            mylist.append(set(inverseIndex[w]))

    # asterisk is splat operator; unzips list
    return set.intersection(*mylist)

