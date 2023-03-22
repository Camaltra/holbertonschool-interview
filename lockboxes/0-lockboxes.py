#!/usr/bin/python3

"""Useless comment"""


def bfs(boxes):
    """
    Make a bfs on the boxes graph to find all possible visitable boxes
    :param boxes: The list of boxes | Graph
    :return: The visited boxes
    """
    visited_boxes = {0}
    queue = {key for key in boxes[0]}
    while queue:
        current_key = queue.pop()
        if current_key in visited_boxes or current_key >= len(boxes):
            continue
        visited_boxes.add(current_key)
        for key in boxes[current_key]:
            if key not in visited_boxes:
                queue.add(key)
    return visited_boxes


def canUnlockAll(boxes):
    """
    Check if we can unlock all boxes
    :param boxes: The list of boxes
    :return: True or False
    """
    if len(boxes) <= 1:
        return True
    visited_boxes = bfs(boxes)
    return len(boxes) == len(visited_boxes)
