#include "lists.h"
/**
 * listint_t - inserts a number into a sorted singly linked list
 * @head: linked list head address pointer
 * @n: element
 *
 * Return:	NULL when there's nothing to insert
 *		new element that's inserted in the list
 */
listint_t *insert_node(listint_t **head, const int n)
{
	listint_t *tmp = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		if (tmp->n >= n)
		{
			new->next = tmp;
			*head = new;
			return (new);
		}
		while (tmp->next && tmp->next->n < n)
			tmp = tmp->next;
		new->next = tmp->next;
		tmp->next = new;
	}
	return (new);
}
