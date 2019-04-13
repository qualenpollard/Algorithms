import sys
from collections import defaultdict
import pprint

graph = defaultdict(list)

def main() :
    
    if len(sys.argv) < 2 :
        print('Error: incorrect format')
        print('Try: python stable_matching_2800144.py inputfile.txt')
        sys.exit(0)
    else :
        root = 0
        with open(sys.argv[1]) as f :
            slurpLine = f.readline().strip()

            try :
                root = int(slurpLine)
                graph[int(slurpLine)].append(int(slurpLine))
            except :
                print("Could not parse integer into graph")
            
            for line in f :
                line = line.strip().split(", ")
                try :
                    graph[int(line[0])].append(int(line[1]))
                except :
                    print("Could not parse integer into graph")
        
        breadthFirstSearch(root)


def breadthFirstSearch(s):
    discovered = [False] * (len(graph))
    discovered[s] = True
    layers = [s]
    tree = []
    
    while layers :

        u = layers.pop(0)
        tree.append(u)

        for v in graph[u] :
            if discovered[v] == False :
                discovered[v] = True
                layers.append(v)
    
    for i in range(len(tree) - 1):
        print(str(tree[i]), end=" ")
    #endfor

    print(str(tree[len(tree) - 1]), end="")
    



if __name__ == '__main__' :
    main()
