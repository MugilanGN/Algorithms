def dijkstra(graph,s):
    
    X = [s]
    A = [0 for i in range(0,200)]
    B = [[] for i in range(0,200)]
    
    while len(X) < 200:
        
        min_w = 0
        min_v = 0
        min_length = 1000000
        
        for v in X:
            for edge in graph[v]:
                w = edge[0]-1
                if w not in X:
                    length = A[v] + edge[1]

                    if min_length > length:
                        min_w = w
                        min_v = v
                        min_length = length
        
        X.append(min_w)
        A[min_w] = min_length
        B[min_w] = B[min_v] + [[min_v,min_w]]
    
    answer = [A[6],A[36],A[58],A[81],A[98],A[114],A[132],A[164],A[187],A[196]]

    print(",".join([str(x) for x in answer]))

def main():
    file = open("Dijkstra.txt", "r+")
    
    graph = [i for i in range(0,200)]
    
    for i,line in enumerate(file):
        
        graph[i] = [[int(x) for x in edge.split(',')] for edge in line.split()[1:]]
        
        print(graph[i])
        
    file.close()
    
    dijkstra(graph,0)
    
if __name__ == "__main__":
    main()