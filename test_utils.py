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
