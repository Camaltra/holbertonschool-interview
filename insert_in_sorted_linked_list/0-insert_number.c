#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a new node in a sorted list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *current = NULL, *previous = NULL;
  listint_t *new_node;

  if (head == NULL)
    return (NULL);

  current = *(head);

  while (current && current->n < number)
  {
    previous = current;
    current = current->next;
  }

  new_node = malloc(sizeof(listint_t));
  if (new_node == NULL)
      return (NULL);

  new_node->n = number;
  new_node->next = current;
  if (previous)
    previous->next = new_node;
  if (current == *head)
    *head = new_node;

  return (new_node);
}
