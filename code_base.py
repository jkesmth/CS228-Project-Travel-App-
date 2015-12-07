
### Utility Functions

def print_formatA(node_list):
    for n in node_list:
        print n.name,
        print ",",

def print_formatB(node_list):
    for n in nodes:
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

    def neighbours(self):
        l = []
        for e in self.edges:
            l.append(e.nodeB)
        return l


class Traveler():

    def __init__(self, start, end):
        self.route = [start]
        self.dest = end
        self.current = start

    def update(self):
        for n in self.current.neighbours(): # testing purposes
            if n not in self.route: # for now just get anything we haven't hit
                self.route.append(n)
                self.current = n
                return self.route
        return None

    

    



        
    



    
    



# main loop v1

##p = Traveler(nodes[0], None)
##print type(p)
##print 
##print "type u to update"
##
##print
##print "started at: ",
##
##print p.current.name
##
##while True:
##    
##    user_input = raw_input('?:')
##    if user_input == "u":
##        next_visited = p.update()
##        if next_visited == None:
##            print "no more places to go, we ",
##            print_format_route(p.route)
##            break
##        else:
##            print_format_route(next_visited)

  

# main loop v2

class Main():
    def __init__(self):
        self.running = False
        self.prompts = ["new = Create a new traveler",
                        "dn = Display the network",
                        "dt = Display the traveler's current route",
                        "u = Update the traveler"
                        "promt = Display prompts"]
        self.inputs = ["new", "dn", "dt", "u", "prompt"]

    
        
    
    def run():
        
        # test case

        entertainment_names = ["Aurora Inn",
                               "Fargo Bar and Grill",
                               "The Well",
                               "The Village Market",
                               "Dinning Hall",
                               "Dorie's",
                               "The Grind",
                               "Koko's"]

        # make the nodes

        nodes = []

        for place in entertainment_names:
            nodes.append(Node(place))

        # network them

        for a in nodes:
            for b in reversed(nodes):
                if a!=b: a.add_edge_to(b)

        # make our starting traveler

        bob = Traveler(nodes[0])

        # start our mainloop
        
        
        self.running = True
        
        for prompt in self.prompts:
            print prompt
        
        while self.running:
            user_input = raw_input("Waiting for input:")
            if user_input not in self.inputs:
                print "Not a valid input"
            if: user_input == self.inputs[0]:
                bob = Traveler(nodes[0])
            if: user_input == self.inputs[1]:
                print_formatB(nodes)
            if: user_input == self.inputs[2]:
                print_format_route(bob.route)
            if: user_input == self.inputs[3]:
                r = bob.update()
                if r != None: print_format_route(r)
                else: print "reached the end"
            if: user_input == self.inputs[4]:
                for prompt in self.prompts:
                    print prompt
                
            
            
            
            
            
            

            
        
        
        



