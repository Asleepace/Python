def wordLadder(beginWord, endWord, wordList):
    return helper(beginWord, endWord, wordList, 0)

def helper(beginWord, endWord, wordList, n):
    
    # Base conditions
    if beginWord == endWord:
        return n+1
    elif n == len(wordList):
        return 0
    
    current = [] # list that is 1 step from current
    newlist = [] # everything else further away
    
    # populate current and newlist
    for i in range(0,len(wordList)):
        if diff(beginWord, wordList[i]) == 1:
            current.append(wordList[i])
        else:
            newlist.append(wordList[i])
    
    distance = 0 # calculated distance
    
    # max distance for each current
    for i in range(0,len(current)):
        length = helper(current[i], endWord, newlist, n+1)
        if distance == 0 and length > 0:
            distance = length
        elif length > 0 and length < distance:
            distance = length
    
    return distance

# calculate difference of two words
def diff(w1,w2):
    c1 = list(w1)
    c2 = list(w2)
    difference = 0
    for i in range(0,len(w1)):
        if c1[i] != c2[i]:
            difference += 1
    return difference
