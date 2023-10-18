#!/usr/bin/python3

"""Useless comment ommmmg"""

def search_island_entry(grid):
    """
    Seach the island entry (The first land, aka the first 1 cell)
    :param grid: The grid
    :return: Tuple of coordinate of the entry or None if no island
    """
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                return x, y
    return None


def check_borders(grid, x, y, visited, to_process):
    """
    Check the border
    If border == 1 and not alredy visited, append to to_process
    If border == 0 or edge, add 1 to perimeter
    :param grid: The grid
    :param x: Current x
    :param y: Current y
    :param visited: Set of visited coordinate
    :param to_process: Set of coordinate to process
    :return:
    """
    current_edges_count = 0
    if x - 1 == -1:
        current_edges_count += 1
    if x + 1 == len(grid):
        current_edges_count += 1
    if y - 1 == -1:
        current_edges_count += 1
    if y + 1 == len(grid):
        current_edges_count += 1

    if grid[x - 1][y] == 0:
        current_edges_count += 1
    elif (x - 1, y) not in visited:
        to_process.add((x - 1, y))

    if grid[x + 1][y] == 0:
        current_edges_count += 1
    elif (x + 1, y) not in visited:
        to_process.add((x + 1, y))

    if grid[x][y - 1] == 0:
        current_edges_count += 1
    elif (x, y - 1) not in visited:
        to_process.add((x, y - 1))

    if grid[x][y + 1] == 0:
        current_edges_count += 1
    elif (x, y + 1) not in visited:
        to_process.add((x, y + 1))

    return current_edges_count


def island_perimeter(grid):
    """
    Compute the island perimeter
    :param grid: The grid represent the island and the water
    :return: The perimeter
    """
    perimeter = 0
    entry_point = search_island_entry(grid)

    if entry_point is None:
        return perimeter

    visited = set()
    to_process = set()

    to_process.add(entry_point)

    while to_process:
        x, y = to_process.pop()
        visited.add((x, y))
        perimeter += check_borders(grid, x, y, visited, to_process)

    return perimeter
