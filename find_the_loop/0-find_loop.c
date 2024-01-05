#include "lists.h"

/**
 * find_listint_loop - Turtle and Hare algo
 *
 * @head: Start of the ll
 *
 * Return: node where loop is located otherwise NULL
 */
listint_t *find_listint_loop(listint_t *head)
{
	listint_t *turtle, *hare;

	turtle = head;
	hare = turtle;
	while (turtle && hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
		{
			turtle = head;
			while (turtle && hare)
			{
				if (turtle == hare)
					return (idk);
				turtle = turtle->next;
				hare = hare->next;
			}
		}
	}
	return (NULL);
}
