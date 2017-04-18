
saved = {}
sizes = {}

def wordLadder(beginWord, endWord, wordList):
    return helper(beginWord, endWord, wordList, 0)

def helper(beginWord, endWord, wordList, n):
    print "n: " + str(n) + " " + beginWord + " " + str(wordList)
    if n > maxes and maxes != 0:
        return 0
    
    if  beginWord in saved:
        return saved[beginWord]
    
    if n > maxes and maxes != 0:
        return 0
    
    # Base conditions
    if beginWord == endWord:
        max_n = n + 1
        return n+1
    elif len(wordList) == 0:
        return 0

    current = [] # list that is 1 step from current
    newlist = [] # everything else further away
    
    to = diff(beginWord,endWord)
    
    # populate current and newlist
    for i in range(0,len(wordList)):
        if diff(beginWord, wordList[i]) == 1:
            if diff(wordList[i], endWord) <= to:
                current.append(wordList[i])
        else:
            newlist.append(wordList[i])
    
    # return if no next iteration
    if len(current) == 0:
        return 0
    
    distance = 0 # calculated distance
    
    # max distance for each current
    for i in range(0,len(current)):
        length = helper(current[i], endWord, newlist, n+1)
            
        if distance == 0 and length > 0:
            distance = length
            saved[current[i]] = length
        elif length > 0 and length < distance:
            distance = length
            saved[current[i]] = length

    
    return distance

# calculate difference of two words
def diff(w1,w2):
    if w1+w2 in sizes:
        return sizes[w1+w2]
    c1 = list(w1)
    c2 = list(w2)
    difference = 0
    for i in range(0,len(w1)):
        if c1[i] != c2[i]:
            difference += 1
    sizes[w1+w2] = difference
    return difference