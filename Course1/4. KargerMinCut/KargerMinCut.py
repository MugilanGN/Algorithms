from random import randrange

def root(graph,elem):
    elem -= 1
    p = graph[elem][0]
    
    while p == 1:
        p = graph[elem][0]
        if p == 1:
            elem = graph[elem][1] - 1
            
    return elem+1    
    
def minCut(graph):
    V = [i for i in range(0,len(graph))]
    
    for i in range(0,len(graph) - 2):
        
        randomVertexIndex = randrange(len(V))
        
        randomVertex = V[randomVertexIndex] + 1
        
        randomEdgeIndex = randrange(len(graph[randomVertex-1][1]))
        
        randomEdge = root(graph,graph[randomVertex-1][1][randomEdgeIndex])
        
        raw_contracted_vertex = graph[randomVertex-1][1]+graph[randomEdge-1][1]

        contracted_vertex = []
        
        for i in range(0,len(raw_contracted_vertex)):
            j = root(graph,raw_contracted_vertex[i])
            if j != randomEdge and j != randomVertex:
                contracted_vertex.append(raw_contracted_vertex[i])

        graph[randomVertex-1] = [1,randomEdge]
        graph[randomEdge-1] = [0,contracted_vertex]
    
        del V[randomVertexIndex]
    
    return int(sum([len(x[1]) for x in graph if x[0] == 0])/2)

def main():
    file = open("KargerMinCut.txt", "r+")

    graph = [[0,[int(x) for x in line.split()][1:]] for i,line in enumerate(file)]
    
    file.close()
    
    minimum = min([minCut(graph.copy()) for i in range(0,100)])
    
    print(minimum)

if __name__ == "__main__":
    main()