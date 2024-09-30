import sys
import Bio

class Graph():
    def __init__(self):
        self.graph = {}

    def add_node(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edges(self, vertex, kmer1, kmer2):
        if kmer1 not in self.graph[vertex] and kmer2 not in self.graph[vertex]:
            self.graph[vertex].append(kmer1)
            self.graph[vertex].append(kmer2)
    
    def adjacency_list(self):
        self.graph = dict(sorted(self.graph.items(), key=lambda x: x[0].lower()) )
        for vertex in self.graph:
            print(f"({self.graph[vertex][0]}, {self.graph[vertex][1]})")


G = Graph()
lines = sys.stdin.readlines()
reverse_complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
rev_kmer = ""

for lin in lines:
    kmer = lin.strip()
    rev = kmer[::-1]
    for i in range(len(rev)):
        rev_kmer += reverse_complement[rev[i]]
    G.add_node(kmer)
    G.add_node(rev_kmer)
    G.add_edges(kmer, kmer[:len(kmer)-1], kmer[1:])
    G.add_edges(rev_kmer, rev_kmer[:len(rev_kmer)-1], rev_kmer[1:]) 
    rev_kmer = ""
G.adjacency_list()