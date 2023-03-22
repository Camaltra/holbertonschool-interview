#!/usr/bin/python3

"""Useless comment"""


def dfs(boxes, keys, visited_boxes):
    """
    Make a dfs on the boxes graph to find all possible visitable boxes
    :param boxes: The list of boxes | Graph
    :param keys: The key to process
    :param visited_boxes: Set of all visited boxes
    :return: Nothing, everything is done by mutating visited_boxes
    """
    for key in keys:
        if key in visited_boxes:
            continue
        visited_boxes.add(key)
        dfs(boxes, boxes[key], visited_boxes)


def canUnlockAll(boxes):
    """
    Check if we can unlock all boxes
    :param boxes: The list of boxes
    :return: True or False
    """
    if len(boxes) <= 1:
        return True
    first_key_list = boxes[0]
    visited_boxes = {0}
    dfs(boxes, first_key_list, visited_boxes)
    return len(boxes) == len(visited_boxes)
