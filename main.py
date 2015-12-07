import sqlite3 as lite




### Utility Functions

def print_formatA(node_list):
    for n in node_list:
        print n.name

def print_formatB(node_list):
    for n in node_list:
        print n.name,
        print "edges:"
        print "-------------------------"*2
        j = 1
        for e in n.edges:
            
            print j,
            
            print "edge from",
            print e.nodeA.name,
            print "to",
            print e.nodeB.name
            
            j += 1
        print "-------------------------"*2
        print

def print_format_route(route):
    print "went to: "
    print "-------------------"*2
    for j in route:
        
        print j.name
    print "-------------------"*2
    print

### Core classes


### this is a basic class which can be used like a C Struct


class Map(dict):
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs) 
        self.__dict__ = self

### "dict" is a python base class which this class is inheriting from
### "super" is another way of refering to the base class
### example of how to use this:
###
###     Yogurt = Map(flavor="blueberry")
###
### this makes a "Map" named "Yogurt" with an atttribute called "flavor"
### that equals "blueberry", ex: Yogurt.flavor = "blueberry"
### it's handy because you can initialize it with any number of arguments
### so it is very flexible

### Node() represents a location on our network
### it has a list of edges which connect it to other nodes
        
class Node():
    
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge_to(self, node):
        edge = Map(nodeA = self, nodeB = node)
        self.edges.append(edge)

    def get_neighbours(self):
        
        neighbor_nodes = []
        for edge in self.edges:
            neighbor_nodes.append(edge.nodeB)
        return neighbor_nodes


class Traveler():

    def __init__(self, start, end = None, blacklist=[]):
        
        self.route = [start]
        self.dest = end
        self.current = start
        self.blacklist = blacklist

    def update(self):
        
        for node in self.current.get_neighbours(): 
            if node not in self.route: 
                self.route.append(node)
                self.current = node
                
        return None  # No more visitable nodes
   

    

    
  



class Main():
    def __init__(self, nodes):

        self.nodes = nodes
        
        # User interface strings
        self.prompts = ["new = Create a new traveler",
                        "dn = Display the network",
                        "dt = Display the traveler's current route",
                        "u = Update the traveler",
                        "x = quit"]
        self.inputs = ["new", "dn", "dt", "u", "x"]

        
    
        
    
    def run(self):

        nodes = self.nodes
        
        # network our nodes (quick and dirty)

        for a in nodes:
            for b in reversed(nodes):
                if a!=b: a.add_edge_to(b)

        # make our starting traveler

        bob = Traveler(nodes[0])

        # start our mainloop
        
        
        running = True
        
        while running:
            for prompt in self.prompts:
                print prompt
            user_input = raw_input("Waiting for input:")
            if user_input not in self.inputs:
                print "Not a valid input"
            if user_input == self.inputs[0]:
                bob = Traveler(nodes[0])
            if user_input == self.inputs[1]:
                print_formatB(nodes)
            if user_input == self.inputs[2]:
                print_format_route(bob.route)
            if user_input == self.inputs[3]:
                r = bob.update()
                if r != None: print_format_route(r)
                else: print "reached the end"
            if user_input == self.inputs[4]:
                running = False
           
           
                
            

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

            
        
        
        



