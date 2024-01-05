#ifndef _BINARY_TREES_H_
#define _BINARY_TREES_H_

/* INCLUDED LIBRARIES */
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

/* STRUCTS AND DEFINITIONS */
/**
 * struct binary_tree_s - Binary tree node
 *
 * @n: Integer stored in the node
 * @parent: Pointer to the parent node
 * @left: Pointer to the left child node
 * @right: Pointer to the right child node
 */
typedef struct binary_tree_s
{
	int n;
	struct binary_tree_s *parent;
	struct binary_tree_s *left;
	struct binary_tree_s *right;
} binary_tree_t;

typedef struct binary_tree_s heap_t;

void binary_tree_print(const binary_tree_t *);

int heap_extract(heap_t **root);
size_t binary_tree_height(heap_t *root);
void find_replacement(heap_t *root, size_t level, heap_t **last);
void free_and_replace(heap_t **root, heap_t **left,
		      heap_t **right, heap_t **last);
void heapify(heap_t **root, heap_t *current, int *check);

#endif /* _BINARY_TREES_H_ */
