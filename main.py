from utils import graph
from model import make_directory, shortest_path, display


GPS = [
    [10.762837665307272, 106.68248927239902], # 1: HCMUS 1
    [10.729770542453958, 106.69583591150504], # 2: RMIT
    [10.78595298610191, 106.70271499895478],  # 3: USSH sdvgs
    [10.82870864214663, 106.70008278179307],  # 4: VLU
    [10.807504346133944, 106.71299161173332], # 5: FTU2
    [10.850637699156412, 106.77191557406877], # 6: HCMUTE dsfdsf
    [10.775225527018806, 106.65777339555909], # 7: HCMUT
    [10.786316917001002, 106.69415444226752], # 8: UEH
    [10.814659721027345, 106.68035473489536], # 9: UFM
    [10.875648150058826, 106.79917031894014], # 10: HCMUS 2 sdvsd
    [10.772521469764833, 106.69801995510616] # Ben Thanh market
]

link = ["www.google.com.br/maps/dir/"]


if __name__ == '__main__':
    coords = GPS
    
    # Dijkstra
    link = ["www.google.com.br/maps/dir/"]
    edges = graph(coords=coords)
    dijkstra_path, dijkstra_weight = shortest_path('dijkstra', coords, edges)
    dijkstra_link = make_directory(link, dijkstra_path, GPS)
    display(dijkstra_path, dijkstra_weight, dijkstra_link, 'dijkstra')

    # Greedy
    link = ["www.google.com.br/maps/dir/"]
    greedy_path, greedy_weight = shortest_path('greedy', coords, edges)
    greedy_link = make_directory(link, greedy_path, GPS)
    display(greedy_path, greedy_weight, greedy_link, 'greedy')
    
    # Astar
    link = ["www.google.com.br/maps/dir/"]
    graph_a, edges_a = graph(coords=coords, algorithm='astar')
    astar_path, astar_weight = shortest_path('astar', coords, edges_a, graph_a)
    astar_link = make_directory(link, astar_path, GPS)
    display(astar_path, astar_weight, astar_link, 'astar')