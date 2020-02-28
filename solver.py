import rubik

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    print("Start:", start, type(start))
    print("End:", end, type(end))

    front = rubik.quarter_twists[0]
    print("Per (F):", front)
    rubik.perm_apply(front, start)
    print("Apply:", start)


    raise NotImplementedError
