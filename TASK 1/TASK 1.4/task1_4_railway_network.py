import csv
import heapq
import os

class RailwayNetwork:
    def __init__(self, csv_file):
        self.graph = {}
        self.load_network_from_csv(csv_file)

    def load_network_from_csv(self, csv_file):
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                station1, station2, cost = row
                cost = int(cost)
                self.add_connection(station1, station2, cost)
                self.add_connection(station2, station1, cost)

    def add_connection(self, station1, station2, cost):
        if station1 not in self.graph:
            self.graph[station1] = []
        self.graph[station1].append((station2, cost))

    def find_cheapest_route(self, departure, destination):
        priority_queue = [(0, departure, [])]
        visited = set()

        while priority_queue:
            current_cost, current_station, current_route = heapq.heappop(priority_queue)

            if current_station in visited:
                continue

            visited.add(current_station)
            current_route = current_route + [current_station]

            if current_station == destination:
                return current_cost, current_route

            for neighbor, cost in self.graph.get(current_station, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (current_cost + cost, neighbor, current_route))

        return float('inf'), []  # No route found

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = "task1_4_railway_network.csv"
    file_path_railway_network = os.path.join(current_dir, file_name)

    railway_network = RailwayNetwork(file_path_railway_network)

    departure = input("Enter the departure station: ").strip()
    destination = input("Enter the destination station: ").strip()

    # Validate input stations
    if departure not in railway_network.graph or destination not in railway_network.graph:
        print("Invalid stations.")
        return

    cheapest_cost, route = railway_network.find_cheapest_route(departure, destination)

    if route:
        print(f"Cheapest cost from {departure} to {destination}: {cheapest_cost}")
        print("Route:", " -> ".join(route))
    else:
        print("No route found.")

if __name__ == "__main__":
    main()