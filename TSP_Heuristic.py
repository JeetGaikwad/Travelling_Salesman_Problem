import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.approximation import traveling_salesman_problem

def generate_complete_graph(num_nodes, weight_range=(1,100)):
  """Generate a complete graph with random edge weights."""
  G = nx.complete_graph(num_nodes)
  for u,v in G.edges():
    G.edges[u,v]['weight'] = random.randint(*weight_range)
  return G

def plot_graph_step(G, tour, current_node, pos):
  """Plot the graph with the current tour and highlighted current node."""
  plt.clf()
  nx.draw(G,pos, with_labels=True, node_color='lightblue', node_size=500)
  path_edges = list(zip(tour, tour[1:]))
  nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
  nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='green', node_size=500)

  edge_labels = nx.get_edge_attributes(G, name='weight')
  nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

  plt.pause(0.5)

def calculate_tour_cost(G, tour):
  """Calculate the total cost of the tour."""
  return sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

def nearest_neighbor_tsp(G, start_node=None):
    """Find an approximate solution to the TSP using the nearest neighbor heuristic."""
    if start_node is None:
        start_node = random.choice(list(G.nodes))

    pos = nx.spring_layout(G)
    plt.ion()
    plt.show()

    unvisited = set(G.nodes)
    tour = [start_node]
    unvisited.remove(start_node)  # Remove the start node from unvisited nodes
    current_node = start_node

    plot_graph_step(G, tour, current_node, pos)

    while unvisited:
        next_node = min(unvisited, key=lambda node: G[current_node][node]['weight'])
        unvisited.remove(next_node)
        current_node = next_node
        tour.append(current_node)  # Append the next node to the tour
        plot_graph_step(G, tour, current_node, pos)

    tour_cost = calculate_tour_cost(G, tour)
    print(f'Construction Heuristic Tour Cost: {tour_cost}')

    plt.ioff()
    plt.show()


if __name__ == '__main__':
  G = generate_complete_graph(6)

  approx_tour = traveling_salesman_problem(G, cycle=True)
  approx_tour_cost = calculate_tour_cost(G, approx_tour)

  print("Nodes in the graph:", list(G.nodes))
  print("approx_tour: ",approx_tour)
  print("approx_tour_cost: ",approx_tour_cost)

  nearest_neighbor_tsp(G, start_node=0)