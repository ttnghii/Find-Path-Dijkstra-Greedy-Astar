from utils import graph
from model import make_directory, shortest_path, shortest_path_astar, display


GPS = [
    [10.762848357761582, 106.68247832592611], # 1: HCMUS 1
    [10.729770542453958, 106.69583591150504], # 2: RMIT
    [10.78595298610191, 106.70271499895478], # 3: USSH
    [10.82870864214663, 106.70008278179307], # 4: VLU
    [10.807504346133944, 106.71299161173332], # 5: FTU2
    [10.853318684005435, 106.77209142581735], # 6: HCMUTE
    [10.775225527018806, 106.65777339555909], # 7: HCMUT
    [10.786316917001002, 106.69415444226752], # 8: UEH
    [10.814659721027345, 106.68035473489536], # 9: UFM
    [10.878883219890747, 106.79906358068935], # 10: HCMUS 2
]

label = ['HCMUS 1', 'RMIT', 'USSH', 'VLU', 'FTU2',
         'HCMUTE', 'HCMUT', 'UEH', 'UFM', 'HCMUS 2']

link = ["www.google.com.br/maps/dir/"]


if __name__ == '__main__':
    coords = GPS
    edges = graph(coords=coords)
    graph_a, edges_a = graph(coords=coords, algorithm='astar')
    
    # [print(f'Label {i + 1}: {label[i]}') for i in range(len(coords))]

    dijkstra_path, dijkstra_weight = shortest_path('dijkstra', coords, edges)
    # greedy_path, greedy_weight = shortest_path('greedy', coords, edges)
    # astar_path, astar_weight = shortest_path_astar(coords, graph_a, edges_a)

    dijkstra_link = make_directory(link, dijkstra_path, GPS)
    # greedy_link = make_directory(link, greedy_path, GPS)
    # astar_link = make_directory(link, astar_path, GPS)

    display(dijkstra_path, dijkstra_weight, dijkstra_link, 'dijkstra')
    # display(greedy_path, greedy_weight, greedy_link, 'greedy')
    # display(astar_path, astar_weight, astar_link, 'astar')