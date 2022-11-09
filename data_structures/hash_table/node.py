class Node:
    def __init__(self, string):
        self.string = string
        self.next = None
    
    def set_next(self, next_node):
        self.next = next_node
    
    def get_next(self):
        return self.next
    

