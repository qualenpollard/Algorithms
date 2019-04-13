import sys
from collections import defaultdict
from collections import deque
import pprint

# Holds the vertices and which vertices they point to.
graph = defaultdict(list)

# Holds the number of edges into a specific vertex.
edgeCount = defaultdict(int)

# Linked list to print topological order.
order = deque()

def main():
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip().split(",")

            try:
                edgeCount[int(line[0])] = edgeCount[int(line[0])]
                edgeCount[int(line[1])] = edgeCount[int(line[1])] + 1
                graph[int(line[0])].append(int(line[1]))

                try:
                    if graph[int(line[1])] != None:
                        continue
                except KeyError:
                    graph[int(line[1])] = {}
            except:
                print("Could not parse integer into graph")
            #endtry
        #endfor
    #endwith

    top_order()

    for i in range(len(order) - 1):
        print(str(order.popleft()), end=" ")
    #endfor
    print(order.popleft(), end=" ")

#enddef

def top_order_recur(vertex):

    for j in graph[vertex]:
        edgeCount[j] = edgeCount[j] - 1
    #endfor

#enddef

def top_order():

    if len(graph) == 0:
        return

    # Find a node v with no incoming edges and order it first 
    for i in sorted(edgeCount.keys()):
        if edgeCount[i] == 0:
            
            order.append(i)
            top_order_recur(i)

            del graph[i]
            del edgeCount[i]
            top_order()

            return
        #endif
    #endfor

#enddef

if __name__ == '__main__':
    main()
