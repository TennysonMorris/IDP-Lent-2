class Robot:
    
    def __init__(self, path, destination):
        self.current_node = 0
        self.current_direction = "N"
        self.current_path = [path]
        self.destination = destination

