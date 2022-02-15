

def extract_distances(json):
    distances_km = []
    routes = json["routes"]
    for route in routes:
        distance_meters = 0
        legs = route["legs"]
        for leg in legs:
            distance_meters += leg["distance"]["value"]
        distances_km.append(distance_meters / 1000)
    return distances_km

