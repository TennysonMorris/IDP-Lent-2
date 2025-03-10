class Robot:
    
    def __init__(self, path, destination):
        self.current_node = 0
        self.current_direction = "N"
        self.current_path = path
        self.pickups = [3, 12, 10, 15]
        self.box_no = 0
        
    def change_path(self, path):
        self.path = path
    
    def change_direction(self, new_direction):
        self.current_direction = new_direction
        
    def next_node(self):
        self.current_node += 1
        
    def next_box(self):
        self.box_no += 1

