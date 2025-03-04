import networkx as nx
import matplotlib.pyplot as plt

# Membuat graf
G = nx.Graph()

# Menambahkan edge sesuai dengan gambar
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
G.add_edges_from(edges)

# Fungsi untuk menampilkan graf
def draw_graph(G):
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G)  # Posisi node
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
    plt.show()

# 1. Mencari Trail dari A ke D (tidak boleh ada edge yang dipakai lebih dari sekali)
def find_trails(graph, start, end):
    return list(nx.all_simple_edge_paths(graph, start, end))

trail_AD = find_trails(G, 'A', 'D')

# 2. Mencari semua Path dari A ke D (tidak boleh ada node yang dikunjungi lebih dari sekali)
all_paths_AD = list(nx.all_simple_paths(G, source='A', target='D'))

# 3. Mencari semua Cycle yang melalui A
cycles_with_A = [cycle for cycle in nx.cycle_basis(G) if 'A' in cycle]

# Menampilkan hasil
print("Trail dari A ke D:", trail_AD)
print("\nSemua Path dari A ke D:", all_paths_AD)
print("\nSemua Cycle yang melalui A:", cycles_with_A)

# Tampilkan visualisasi graf
draw_graph(G)