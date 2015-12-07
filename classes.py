import sqlite3 as lite



class Map(dict):
    """Utility function used to quickly encapsulate data"""
    
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs) 
        self.__dict__ = self

        
class Node():
    """Base location class"""
    
    def __init__(self, name=None):
        """Option to give a unique identifier"""
        self.name = name
        self.edges = []

    def add_edge_to(self, node):
        """Adds an edge from this Node to another Node"""
        
        edge = Map(nodeA = self, nodeB = node)
        self.edges.append(edge)

    def get_neighbours(self):
        """Returns all Nodes connected to this Node via edges"""
        
        neighbor_nodes = []
        for edge in self.edges:
            neighbor_nodes.append(edge.nodeB)
        return neighbor_nodes


class Traveler():
    """Travels a network of Nodes"""

    def __init__(self, start, end = None):
        """Initialized with a starting location and optional destination"""
        
        self.route = [start]
        self.dest = end
        self.current = start
    
    def update(self):
        """Called every time the traveler needs to move to a new node"""
        
        for node in self.current.get_neighbours(): 
            if node not in self.route: 
                self.route.append(node)
                self.current = node
                
        return None  # No more visitable nodes
   

    

    
  



           
                
            

# Remake our test database        

execfile('construct_database.py')

# Grab the data we want from the database

con = lite.connect('test_database.db')

node_list = []

with con:

    con.row_factory = lite.Row
    
    cur = con.cursor()
    cur.execute("SELECT * FROM venues")
    
    rows = cur.fetchall()
    
    for row in rows:
        node_list.append(Node(row["name"]))



m = Main(node_list)

m.run()        

            
        
        
        



