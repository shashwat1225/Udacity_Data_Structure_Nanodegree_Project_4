     
def shortest_path(_map,start,goal):
    navigator = AStar(_map)
    output = navigator.shortest_path(start,goal)
    return output
