from utils import graph
from model import make_directory, shortest_path, shortest_path_astar, display


GPS = [
    [10.762861, 106.682472], # 1: HCMUS 1
    [10.729189, 106.695783], # 2: RMIT
    [10.785861, 106.702722], # 3: USSH
    [10.827829, 106.700567], # 4: VLU
    [10.806762, 106.712719], # 5: FTU2
    [10.850631, 106.771937], # 6: HCMUTE
    [10.773267, 106.659466], # 7: HCMUT
    [10.783258, 106.694751], # 8: UEH
    [10.811472, 106.680583], # 9: UFM
    [10.875658, 106.799184], # 10: HCMUS 2
]

label = ['HCMUS 1', 'RMIT', 'USSH', 'VLU', 'FTU2',
         'HCMUTE', 'HCMUT', 'UEH', 'UFM', 'HCMUS 2']

link = ["www.google.com.br/maps/dir/"]


if __name__ == '__main__':
    coords = GPS
    edges = graph(coords=coords)
    graph_a, edges_a = graph(coords=coords, algorithm='astar')
    
    [print(f'Label {i + 1}: {label[i]}') for i in range(len(coords))]

    dijkstra_path, dijkstra_weight = shortest_path('dijkstra', coords, edges)
    greedy_path, greedy_weight = shortest_path('greedy', coords, edges)
    astar_path, astar_weight = shortest_path_astar(coords, graph_a, edges_a)

    dijkstra_link = make_directory(link, dijkstra_path, GPS)
    greedy_link = make_directory(link, greedy_path, GPS)
    astar_link = make_directory(link, astar_path, GPS)

    display(dijkstra_path, dijkstra_weight, dijkstra_link, 'dijkstra')
    display(greedy_path, greedy_weight, greedy_link, 'greedy')
    display(astar_path, astar_weight, astar_link, 'astar')