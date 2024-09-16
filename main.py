from utils import graph
from model import make_directory, shortest_path, display


GPS = [
    [10.762594978993034, 106.68237792927061], # 1: HCMUS 1
    [10.796886429503637, 106.6736746466129],  # 2: VAA
    [10.78595298610191, 106.70271499895478],  # 3: USSH
    [10.762763157666535, 106.69330582535177], # 4: VLU 
    [10.806767109442625, 106.7127273625484],  # 5: FTU2 
    [10.850637699156412, 106.77191557406877], # 6: HCMUTE 
    [10.858151533975555, 106.75577395543505], # 7: People's Police University
    [10.78309312528787, 106.69474336667191],  # 8: UEH 
    [10.781990133934986, 106.6944889135089],  # 9: UAH
    [10.875648150058826, 106.79917031894014], # 10: HCMUS 2 
]


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