import rubik

def bfs(start, end):
    # Create subarray
    queue = list()
    visited = list()

    queue.append({'perm':start, 'moves':visited})
    print(type(visited))
    while queue or (len(visited) < 15):
        current = queue.pop(0)
        print(current)
        visited = current['moves']
        if current['perm'] != end:
            for m in range(len(rubik.quarter_twists)):
                move = rubik.quarter_twists[m]
                print('Tuple:', visited, type(visited))
                poss = rubik.perm_apply(move, current['perm'])
                moves = []
                moves = moves + visited
                moves.append(move)
                print(moves)
                queue.append({'perm':poss,'moves':moves})

        else:
            return current['moves']
    
    return None

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    print("Start:", start, type(start))
    print("End:", end, type(end))

    print("New node:", end)
    rubik.perm_apply(rubik.F, end)
    print("New node:", end)
    rubik.perm_apply(rubik.F, end)
    print("New node:", end)
    return bfs(start,end)

    raise NotImplementedError
