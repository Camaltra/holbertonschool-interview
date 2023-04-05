#include <stdlib.h>
#include "binary_trees.h"

/**
 * binary_tree_node -- Insert a node into a binary tree
 *
 * @parent: The node parent
 * @value: The value of the new node
 *
 * Return: The the create node adresses
 */
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
  binary_tree_t *node_to_insert = NULL;

  node_to_insert = malloc(sizeof(binary_tree_t));
  if (!node_to_insert)
    return NULL;

  node_to_insert->n = value;
  if (parent)
  {
    node_to_insert->parent = parent;
    if (!parent->left)
      parent->left = node_to_insert;
    else
      parent->right = node_to_insert;
  }
  else
    node_to_insert->parent = NULL;
  node_to_insert->left = NULL;
  node_to_insert->right = NULL;

  return (node_to_insert);
}
