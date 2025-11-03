# F1 Calendar Route Optimiser

A Python-based optimisation tool that analyzes Formula 1 race calendar locations and finds more efficient routing using the nearest neighbor algorithm.

## Project Overview

This project was originally developed in **August 2023** as part of a high school research paper to explore optimisation algorithms and their real-world applications. It calculates the total travel distance for the official F1 calendar order and compares it with an optimized route that minimizes total distance traveled.

**Note:** This code was written in 2023 and is being published to GitHub in 2025 as part of building a portfolio of past work.

## Features

- **Haversine Distance Calculation**: Accurately calculates great-circle distances between race locations
- **Nearest Neighbor Algorithm**: Implements a greedy heuristic to optimise travel routes
- **Comparison Analysis**: Shows distance savings between official and optimised calendars
- **23 Race Locations**: Covers all major F1 circuits from the 2023 season

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rsilinevich/f1-calendar-optimiser
cd f1-calendar-optimiser
```

2. Run the script:
```bash
python f1-calendar-optimiser.py
```

## How It Works

### Algorithm

The program uses a **nearest neighbor algorithm**, which:
1. Starts at the first location
2. Finds the closest unvisited location
3. Travels there and repeats until all locations are visited

### Distance Calculation

Uses the **Haversine formula** to calculate distances between coordinates:
```
a = sin²(Δφ/2) + cos φ1 × cos φ2 × sin²(Δλ/2)
c = 2 × atan2(√a, √(1−a))
d = R × c
```

Where φ is latitude, λ is longitude, and R is Earth's radius (6,371 km)

## Result

```
Official Calendar Order
============================================================
 1. Bahrain              → Saudi Arabia         (1258.37 km)
 2. Saudi Arabia         → Australia            (12817.26 km)
 3. Australia            → Azerbaijan           (12990.24 km)
...
Total distance: 132165.18 km

Optimised Route (Nearest Neighbor)
============================================================
 1. Bahrain              → Qatar                ( 112.46 km)
 2. Qatar                → Abu Dhabi            ( 336.95 km)
 3. Abu Dhabi            → Saudi Arabia         (1616.09 km)
...
Total distance: 56440.89 km

Distance saved: 75724.29 km (57.3%)
```

## Limitations

- **Nearest neighbor is a greedy algorithm** - it doesn't guarantee the optimal solution
- **Doesn't account for**: logistics constraints, seasonal weather, venue availability, broadcast schedules, or geopolitical factors
- **Real F1 calendar** considers many non-distance factors in scheduling

## Potential Improvements

- Implement 2-opt or 3-opt optimisation for better results
- Add genetic algorithm or simulated annealing
- Include time zone considerations
- Factor in seasonal climate patterns
- Visualize routes on a world map

## Educational Value

This project demonstrates:
- Practical application of optimisation algorithms
- Geographic coordinate systems and distance calculations
- Trade-offs between algorithm complexity and solution quality
- The traveling salesman problem (TSP) in a real-world context

## Author
Developed by **Raimonds Siliņevičs**  
Originally written in 2023, published in 2025.
