#  Utility functions.  
def print_nodes(node_l):
    for n in node_l:
        print n.name,
        print n.cost


#  Structs

class Node():

    def __init__(self, edges = [], cost = 0, name = ""):
        
        self.edges = edges

        self.cost = cost

        self.name = name

    def add_edge(self, edge):

        self.edges.append(edge)

class Edge():

    def __init__(self, two_nodes, cost = 0):
        
        self.nodes = (two_nodes[0], two_nodes[1])

        self.cost = cost

    

class Network():
    
    def __init__(self, nodes = []):
        
        self.nodes = nodes

    def add_node(self, new_node):
        
        if new_node not in self.nodes:
            
            for node in self.nodes:
                
                e = Edge((new_node, node))
                node.add_edge(e)
                new_node.add_edge(e)
                
            self.nodes.append(new_node)
            
  

#  Network traveling.

class Traveler():

    def __init__(self, budget = 0):

        self.budget = budget

    def travel_net(self, start_node):

        ### Returns a path
        
        path = Path(start_node)
        
        pos = start_node

        
        while pos != False:
            
            pos = path.next_node(pos)
        
        return path
            

class Path():
    
    def __init__(self, start):
        self.start = start
        self.route = []

        self.blacklist = []

        self.add_pos(start)

    def add_pos(self, pos):
        
        self.route.append(pos)
        self.set_traveled(pos)

    def next_node(self, prev_node):
        if not prev_node == False:
            for edge in prev_node.edges:
                if not edge in self.blacklist:
                    for node in edge.nodes:
                        if node not in self.blacklist:
                            self.set_traveled(node)
                            return node
        return False

    def set_traveled(self, traveled):
        
        self.blacklist.append(traveled)
        



        


#  Test cases.


p, g, f, h = (Node(cost=10, name="Aurora Inn"), Node(cost=8, name="Fargo"),
              Node(cost=6, name="Well"), Node(cost=4, name="Market"))

n_list = [p, g, f, h]

net = Network()

for n in n_list:
    net.add_node(n)
        
print_nodes(net.nodes)

t = Traveler()

went = t.travel_net(p)


  
