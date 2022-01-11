import sys

class node:
    def __init__(self, value:int):
        self.value = value
        self.leaderPointer = None
        self.adjList = []
    def setLeaderPointer(self, leaderPointer:int):
        self.leaderPointer = leaderPointer

class Weighted_Edge:
    def __init__(self, node_number:int, weight:int):
        self.weight = weight
        self.node_number = node_number

class Graph:
    def __init__(self, n_nodes:int):
        n_nodes = int(n_nodes)
        self.nodes = [None]*n_nodes #create a None array of no of nodes
        #initialize all the nodes
        for i in range(0, n_nodes):
            self.nodes[i] = node(i)

    def add_edge(self, src:int, dest:int, weight:int):
        temp_edge = Weighted_Edge(dest, weight)
        self.nodes[int(src)].adjList.append(temp_edge)
    
    

class Edge_Instance:
    def __init__(self, src:int, dest:int, weight:int):
        self.src = src
        self.dest = dest
        self.weight = weight

def union(G:Graph, src:int, dest:int):
    print('union')
    src_leaderPointer = G.nodes[src].leaderPointer
    dest_leaderPointer = G.nodes[dest].leaderPointer
    for i5 in range(len(G.nodes)):
        print('for')
        
        if(G.nodes[i5].leaderPointer == src_leaderPointer):
            print('hi')
            G.nodes[i5].setLeaderPointer(dest_leaderPointer)
        #if(G.nodes[i5].leaderPointer == src):
       #     print('hi')
         #   G.nodes[i5].setLeaderPointer(dest)

def kruskal(G:Graph):
    MST = []
################################ Make set (V) #########################################
    for i3 in range(len(G.nodes)):
        G.nodes[i3].leaderPointer = G.nodes[i3].value
##################################################################################

################Sort the edges#################################################    
    edge_list = [] #list of edges
    for i in range(len(G.nodes)):
        i1 = 0 #start number of adjacency node = 0
        temp_node = G.nodes[i]
        adj_node = len(temp_node.adjList)
        while(adj_node):
            temp_edge_instance = Edge_Instance(i, temp_node.adjList[i1].node_number, G.nodes[i].adjList[i1].weight)
            edge_list.append(temp_edge_instance)
            i1+=1
            adj_node -= 1

    for i2 in range(len(edge_list)):
        print(edge_list[i2].src, edge_list[i2].dest, edge_list[i2].weight)
    print('sorting')
    edge_list.sort(key=lambda x : int(x.weight), reverse=False)

    for i2 in range(len(edge_list)):
        print(edge_list[i2].src, edge_list[i2].dest, edge_list[i2].weight)
    
  
    
#############################edges sorted################################################
    for i4 in range(len(edge_list)):
        print(G.nodes[int(edge_list[i4].src)].value, G.nodes[int(edge_list[i4].src)].leaderPointer, G.nodes[int(edge_list[i4].dest)].value, G.nodes[int(edge_list[i4].dest)].leaderPointer)
        if(G.nodes[int(edge_list[i4].src)].leaderPointer != G.nodes[int(edge_list[i4].dest)].leaderPointer):
            MST.append(edge_list[i4])
            union(G, G.nodes[int(edge_list[i4].src)].value, G.nodes[int(edge_list[i4].dest)].value)

    #############################calculate total weight###########################################################
    total_MST_weight = 0
    total_MST_weight = int(total_MST_weight)
    for i6 in range(len(MST)):
        total_MST_weight = total_MST_weight + int(MST[i6].weight)
        print(MST[i6].src, MST[i6].dest, MST[i6].weight)
    
    print('total weight = ', total_MST_weight)


if __name__ == "__main__":
    n_nodes = input('Enter number of nodes in the graph: ')
    G = Graph(n_nodes)
    while(True):
        temp_src, temp_dest, temp_weight = input("Print source, destination and edge weight: ").split()
        G.add_edge(temp_src, temp_dest , temp_weight)
        temp = input("Do you wish to continue adding edges?(0/1): ")
        if(temp == '0'):
            break
    
    kruskal(G)
