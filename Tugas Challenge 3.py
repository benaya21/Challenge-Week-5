import matplotlib.pyplot as plt
import networkx as nx

def create_graph():
    G = nx.Graph()
    edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('C', 'E'), ('C', 'F'),
             ('D', 'F'), ('E', 'G'), ('E', 'H'), ('F', 'I'), ('F', 'J'), ('G', 'K'),
             ('H', 'K'), ('I', 'K'), ('J', 'K')]
    G.add_edges_from(edges)
    return G

def draw_graph(G):
    pos = {'A': (2, 5), 'B': (1, 4), 'C': (2, 4), 'D': (3, 4), 'E': (1.5, 3),
           'F': (2.5, 3), 'G': (0.5, 2), 'H': (1.5, 2), 'I': (2.5, 2), 'J': (3.5, 2), 'K': (2, 1)}
    
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
    plt.show()

def find_all_paths(G, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in G:
        return []
    paths = []
    for node in G[start]:
        if node not in path:
            new_paths = find_all_paths(G, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths

def find_cycles(G, start):
    cycles = []
    def dfs(node, visited, path):
        visited.add(node)
        path.append(node)
        for neighbor in G[node]:
            if neighbor == start and len(path) > 2:
                cycles.append(list(path))
            elif neighbor not in visited:
                dfs(neighbor, visited, path)
        path.pop()
        visited.remove(node)
    dfs(start, set(), [])
    return cycles

def main():
    G = create_graph()
    draw_graph(G)
    
    print("Semua Path dari A ke K:", find_all_paths(G, 'A', 'K'))
    print("Semua Path dari G ke J:", find_all_paths(G, 'G', 'J'))
    print("Semua Path dari E ke F:", find_all_paths(G, 'E', 'F'))
    print("Semua Cycle jika A titik awal:", find_cycles(G, 'A'))
    print("Semua Cycle jika K titik awal:", find_cycles(G, 'K'))
    
    paths_AK = find_all_paths(G, 'A', 'K')
    paths_GJ = find_all_paths(G, 'G', 'J')
    paths_EF = find_all_paths(G, 'E', 'F')
    
    print("Circuit Terpendek dari A ke K:", min(paths_AK, key=len) if paths_AK else [])
    print("Circuit Terpanjang dari A ke K:", max(paths_AK, key=len) if paths_AK else [])
    print("Circuit Terpendek dari G ke J:", min(paths_GJ, key=len) if paths_GJ else [])
    print("Circuit Terpanjang dari G ke J:", max(paths_GJ, key=len) if paths_GJ else [])
    print("Circuit Terpendek dari E ke F:", min(paths_EF, key=len) if paths_EF else [])
    print("Circuit Terpanjang dari E ke F:", max(paths_EF, key=len) if paths_EF else [])

main()