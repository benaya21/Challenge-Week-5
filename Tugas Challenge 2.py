import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

def draw_graph(graph, paths=None, cycles=None):
    pos = {
        'A': (0, 2), 'B': (2, 3), 'C': (4, 2),
        'D': (0, 0), 'E': (2, 1), 'F': (4, 0)
    }
    
    plt.figure(figsize=(6,6))
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='lightblue', edge_color='gray')
    
    if paths:
        for path in paths:
            edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='blue', width=2)
    
    if cycles:
        for cycle in cycles:
            edges = [(cycle[i], cycle[i+1]) for i in range(len(cycle)-1)] + [(cycle[-1], cycle[0])]
            nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='red', width=2)
    
    plt.show()

def find_paths_cycles():
    edges = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('C', 'F'),
             ('D', 'E'), ('E', 'F'), ('B', 'D'), ('C', 'E')]
    G = nx.Graph()
    G.add_edges_from(edges)
    
    start, end = 'A', 'C'
    paths = list(nx.all_simple_paths(G, source=start, target=end))
    print("Semua kemungkinan Path dari A ke C:", paths)
    
    cycles_c = list(nx.simple_cycles(nx.DiGraph(G.subgraph(nx.node_connected_component(G, 'C')))))
    print("Semua kemungkinan Cycle jika C adalah titik awal:", cycles_c)
    
    cycles_b = list(nx.simple_cycles(nx.DiGraph(G.subgraph(nx.node_connected_component(G, 'B')))))
    print("Semua kemungkinan Cycle jika B adalah titik awal:", cycles_b)
    
    shortest_path = min(paths, key=len) if paths else []
    longest_path = max(paths, key=len) if paths else []
    print("Circuit Terpendek dari A ke C:", shortest_path)
    print("Circuit Terpanjang dari A ke C:", longest_path)
    
    draw_graph(G, paths=paths, cycles=cycles_c + cycles_b)

find_paths_cycles()
