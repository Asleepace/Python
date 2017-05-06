def stringsRearrangement(a):
    
    graph = graphArray(a)
    
    if graph == None: return False
    

    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if i == j: continue
            path = findPath(graph, i, j, [])
            if path != None: return True
                
    
    return False
                
def findPath(graph, start, end, path=[]):
    print path
    path.append(start)
    
    if start == end: return path
    if not graph.has_key(start): return None
    
    for node in graph[start]:
        if node not in path:
            newPath = findPath(graph, node, end, list(path))
            if newPath:
                hamiltonian = True
                for key in graph:
                    if key not in newPath:
                        hamiltonian = False
                if hamiltonian: return newPath
            
    return None
        
         
def graphArray(a):
    graph = {}
    for i, word1 in enumerate(a):
        graph[i] = []
        for j, word2 in enumerate(a):
            if i == j: continue
            if diff(word1,word2) == 1:
                graph[i].append(j)
    return graph
    


def diff(s1, s2):
    d = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: d+=1
    return d