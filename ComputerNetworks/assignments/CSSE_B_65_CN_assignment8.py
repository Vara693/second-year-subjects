import math

class Router:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors  
        self.distance_vector = {name: 0}
        
        for n, cost in neighbors.items():
            self.distance_vector[n] = cost

    def update(self, network):
        updated = False
        
        for dest in network:
            if dest == self.name:
                continue

            min_cost = math.inf
            
            for neighbor, cost_to_neighbor in self.neighbors.items():
                neighbor_router = network[neighbor]
                neighbor_cost = neighbor_router.distance_vector.get(dest, math.inf)
                
                total_cost = cost_to_neighbor + neighbor_cost
                
                if total_cost < min_cost:
                    min_cost = total_cost

            if dest not in self.distance_vector or self.distance_vector[dest] != min_cost:
                self.distance_vector[dest] = min_cost
                updated = True
        
        return updated


def distance_vector_routing(network):
    routers = {name: Router(name, neighbors) for name, neighbors in network.items()}
    
    iteration = 0
    while True:
        print(f"\nIteration {iteration}")
        stable = True
        
        for router in routers.values():
            if router.update(routers):
                stable = False
        
        for name, router in routers.items():
            print(f"{name}: {router.distance_vector}")
        
        iteration += 1
        
        if stable:
            break

    return routers


network = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 7},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

distance_vector_routing(network)