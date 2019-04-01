import sys
from collections import defaultdict
import pprint

graph = defaultdict(list)


def main():

    if len(sys.argv) < 2:
        print('Error: incorrect format')
        print('Try: python dfs_Pollard.py inputfile.txt')
        sys.exit(0)
    else:
        with open(sys.argv[1]) as f :
            head = f.readline().strip()

            for line in f :
                line = line.strip().split(", ")
                try:
                    graph[int(line[0])].append(int(line[1]))
                except:
                    print("Could not parse integer into graph")

        depthFirstSearch(int(head))


def depthFirstSearch(s) :
    explored = [False] * (max(graph) * 2)

    #Initialize S to be a stack with one element s
    stack = [s]

    while stack :
        #Take a node u from stack
        u = stack.pop(0)
        print(u)

        if explored[u] == False :
            explored[u] = True

            for v in graph[u] :
                stack.append(v)
            #rof
        #fi
    #elihw
#fed


if __name__ == '__main__':
    main()
