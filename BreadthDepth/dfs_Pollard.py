import sys
from collections import defaultdict
from collections import deque
import pprint

graph = defaultdict(list)


def main():

    if len(sys.argv) < 2:
        print('Error: incorrect format')
        print('Try: python dfs_Pollard.py inputfile.txt')
        sys.exit(0)
    else:
        root = 0
        with open(sys.argv[1]) as f :
            slurpLine = f.readline().strip()

            try:
                root = int(slurpLine)
            except:
                print("Could not parse integer into graph")

            for line in f :
                line = line.strip().split(", ")
                try:
                    graph[int(line[0])].append(int(line[1]))
                except:
                    print("Could not parse integer into graph")

        depthFirstSearch(root)


def depthFirstSearch(s) :
    explored = [False] * (len(graph))

    #Initialize S to be a stack with one element s
    stack = []
    stack.append(s)

    tree = []

    while stack :

        #Take a node
        u = stack.pop()

        if explored[u] == False :
            explored[u] = True
            tree.append(u)

            for v in range(len(graph[u])-1, -1, -1) :
                stack.append(graph[u][v])
    
    for i in tree:
        print(i, end=" ")


if __name__ == '__main__':
    main()
