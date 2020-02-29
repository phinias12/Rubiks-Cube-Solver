import rubik

def getFrontier(queue, visit):
    parents = [] + queue
    while parents:
        p = parents.pop(0)
        visited = p['moves']
        queue.pop(0)
        for m in range(len(rubik.quarter_twists)):
            move = rubik.quarter_twists[m]
            poss = rubik.perm_apply(move, p['perm'])
            moves = []
            moves = moves + visited
            moves.append(move)
            queue.append({'perm': poss,'moves':moves})
            
            if poss not in visit:
                visit[poss] = []

            node = visit[poss]
            node.append(moves)

def compareFrontier(right, left):
    r_keys = right.keys()
    for r in r_keys:
        if r in left:
            l_moves = left[r]
            r_moves = right[r]
            result = []

            for ri in r_moves:
                inverse_moves = []
                for le in l_moves:
                    inverse_moves = le
                    getInverse(inverse_moves)
                
                if inverse_moves.reverse() != ri:
                    result = ri + inverse_moves
            
                    return result

    return None

def getInverse(moves):
    for m in range(len(moves)):
        moves[m] = rubik.perm_inverse(moves[m])

def r_bfs(start, end):
    s_enq = [{'perm':start,'moves':[]}]
    e_enq = [{'perm':end,'moves':[]}]
    s_visited = {start:[]}
    e_visited = {end: []}
    depth = 1

    if start == end:
        return []

    while depth < 8:
        check = compareFrontier(s_visited, e_visited)
        if check != None:
            return check

        getFrontier(s_enq, s_visited)
        check = compareFrontier(s_visited, e_visited)
        if check != None:
            return check

        getFrontier(e_enq, e_visited)
        check = compareFrontier(s_visited, e_visited)
        if check != None:
            return check

        depth = depth + 1

    return None

# Main function
def bfs(start, end):
    # Create subarray
    queue = list()
    visited = list()

    queue.append({'perm':start, 'moves':visited})
    while queue or (len(visited) < 15):
        current = queue.pop(0)
        visited = current['moves']
        if current['perm'] != end:
            for m in range(len(rubik.quarter_twists)):
                move = rubik.quarter_twists[m]
                poss = rubik.perm_apply(move, current['perm'])
                moves = []
                moves = moves + visited
                moves.append(move)
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
    
    return r_bfs(start,end)
