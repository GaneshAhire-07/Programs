import numpy as np
import matplotlib.pyplot as plt
import random

# Read city data from file
def read_cities(filename):
    cities = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            name = parts[0]
            x, y = float(parts[1]), float(parts[2])
            cities.append((name, x, y))
    return cities

cities = read_cities('India_cities.txt')

# Calculate the Euclidean distance between two points
def distance(city1, city2):
    return np.sqrt((city1[1] - city2[1])**2 + (city1[2] - city2[2])**2)

# Calculate the total distance of a path
def total_distance(cities, path):
    dist = 0.0
    for i in range(len(path)):
        dist += distance(cities[path[i]], cities[path[(i + 1) % len(path)]])
    return dist

# Perform a simulated annealing optimization
def simulated_annealing(cities, initial_temp, cooling_rate, max_iterations):
    n = len(cities)
    current_path = list(range(n))
    random.shuffle(current_path)
    current_distance = total_distance(cities, current_path)

    best_path = list(current_path)
    best_distance = current_distance

    temperature = initial_temp

    for iteration in range(max_iterations):
        i, j = sorted(random.sample(range(n), 2))
        new_path = current_path[:i] + current_path[i:j+1][::-1] + current_path[j+1:]
        new_distance = total_distance(cities, new_path)

        if new_distance < current_distance or random.random() < np.exp((current_distance - new_distance) / temperature):
            current_path, current_distance = new_path, new_distance

        if new_distance < best_distance:
            best_path, best_distance = new_path, new_distance

        temperature *= cooling_rate

        if iteration % 100 == 0:
            print(f"Iteration {iteration}: Best Distance = {best_distance}")

    return best_path, best_distance

# Plot the cities and the path
def plot_cities(cities, path):
    x = [cities[i][1] for i in path] + [cities[path[0]][1]]
    y = [cities[i][2] for i in path] + [cities[path[0]][2]]
    names = [cities[i][0] for i in path]

    plt.figure(figsize=(10, 8))
    plt.plot(x, y, 'o-', markersize=10, lw=2)
    for i, name in enumerate(names):
        plt.text(x[i], y[i], name, fontsize=12, ha='right')
    plt.title("Traveling Salesman Path")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.show()

# Test the simulated annealing function and plot the result
initial_temp = 1000
cooling_rate = 0.995
max_iterations = 1000

best_path, best_distance = simulated_annealing(cities, initial_temp, cooling_rate, max_iterations)
plot_cities(cities, best_path)
