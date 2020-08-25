class Vertex:
    def __init__(self, city):
        self.city = city
        self.edges = {}

    def add_edge(self, city, info):
        self.edges[city] = info

    def get_edge(self):
        return self.edges.keys()

class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.vertices[vertex.city] = vertex

    def add_edge(self, vertex_a, vertex_b, cost, time):
        self.vertices[vertex_a.city].add_edge(vertex_b.city, {'cost': cost, 'time': time})

        if not self.directed:
            self.vertices[vertex_b.city].add_edge(vertex_a.city, {'cost': cost, 'time': time})

    def path_exists(self, vertex_a, vertex_b):
        to_visit = [vertex_a]
        visited = []

        while to_visit:
            current_city = to_visit.pop(0)
            visited.append(current_city)
            if current_city == vertex_b:
                return True
            else:
                vertices = self.vertices[current_city].edges.keys()
                to_visit += [vertex for vertex in vertices if vertex not in visited]
        return False


airline = Graph(directed=False)

cities = [
Vertex("Kuwait"), Vertex("Dubai"), Vertex("Colombo"), Vertex("Male"),
Vertex("Doha"), Vertex("Tokyo"), Vertex("Oslo")
]

for city in cities:
    airline.add_vertex(city)


airline.add_edge(cities[0], cities[1], 120, 2)
airline.add_edge(cities[0], cities[2], 200, 4)
airline.add_edge(cities[2], cities[3], 60, 1)
airline.add_edge(cities[1], cities[4], 100, 1.5)
airline.add_edge(cities[4], cities[5], 500, 11)
airline.add_edge(cities[1], cities[6], 300, 6)



print("-"*90)
print("Our destinations that you can travel to through out Airline: ")
print("-"*90)

for city in airline.vertices.keys():
    print(f"-   {city}")

print("-"*90)
travel_from = input("Select a City you want to travel to through our awesome Airline: ")

print("-"*90)
print(f"The destinations you can travel to from {travel_from}: ")
print("-"*90)
for destination in airline.vertices[travel_from].get_edge():
    print(f"-   {destination}")

print("-"*90)
travel_to = input("Select a City: ")

info = airline.vertices[travel_from].edges[travel_to]

print(f"The flight will take {info['time']} hours and it will cost {info['cost']}$")
