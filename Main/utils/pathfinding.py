## create map as dictionary
from settings import Robot

map = {
    0 : {"N" : 1},
    1 : {"W" : 2, "E" : 18},
    2 : {"N" : 3, "W" : 4, "E" : 1},
    3 : {"S" : 2},
    4 : {"N" : 6, "S" : 5, "E" : 2},
    5 : {"N" : 4},
    6 : {"N" : 7, "S" : 4, "E" : 11},
    7 : {"E" : 8, "S" : 6},
    8 : {"S" : 9, "E" : 14, "W" : 7},
    9 : {"N" : 8, "W" : 10, "S" : 11},
    10 : {"E" : 9},
    11 : {"N" : 9, "W" : 6, "E" : 12},
    12 : {"S" : 13, "W" : 11, "E" : 17},
    13 : {"N" : 12},
    14 : {"W" : 8, "E": 16, "S" : 15},
    15 : {"N" : 14},
    16 : {"W" : 14, "S" : 17},
    17 : {"W" : 12, "S" : 18, "N" : 16},
    18 : {"N" : 17, "W" : 1, "S" : 19},
    19 : {"N" : 18}
}

##turn logic
turn_logic = {
    "N": {"N": "Straight", "E": "Right", "W": "Left"},
    "S": {"S": "Straight", "E": "Left", "W": "Right"},
    "E": {"E": "Straight", "S": "Right", "N": "Left"},
    "W": {"W": "Straight", "S": "Left", "N": "Right"}
}

#get available moves at any node
def moves(node):
    return map.get(node)

##shortest paths between key points
paths = {
    #start to pickup points
    0 : {3 : [0,1,2,3], 10 : [0,1,2,4,6,11,9,10], 15 : [0,1,18,17,16,14,15], 13 : [0, 1,18,17,12,13]},
    #depots to pickup points and start
    5 : {3 : [5,4,2,3], 10 : [5,4,6,11,9,10], 15 : [5,4,6,7,8,14,15], 13 : [5,4,6,11,12,13], 0 : [5,4,2,1,0]},
    19 : {3 : [19,18,1,2,3], 10 : [19,18,17,12,11,9,10], 15 : [19,18,17,16,14,15], 13 : [19,18,17,12,13], 0 :[19,18,1,0]},
    #pick up points to depot
    3 : {5 : [3,2,4,5], 19: [3,2,1,18,19]},
    10 : {5 : [10,9,11,6,4,5], 19: [10,9,11,12,17,18,19]},
    15 : {5 : [15,14,8,7,6,4,5], 19: [15,14,16,17,18,19]},
    13 : {5 : [13,12,11,6,4,5], 19: [13,12,17,18,19]}
}

def set_path(current_node, destination):
    return paths[current_node][destination]
    

def turn_direction(robot):
    
    ##get available moves
    moves = moves(robot.current_path[robot.current_node])

    ##based on next node, find direction needed
    for i in moves:
        if moves[i] == robot.current_path[robot.current_node + 1]:
            next_direction = i
            break
    
    ##return turn direction
    return next_direction, turn_logic[robot.current_direction][next_direction]

    
    
    


