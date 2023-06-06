#include "lists.h"
/**
 * check_cycle - checks if a cycle is present in a singly linked list
 * @list: singly linked list
 *
 * Return:  0 when there's no cycle
 *      1 when a cycle is present
 */
int check_cycle(listint_t *list)
{
	listint_t *elm1, *elm2;

	if (list == NULL || list->next == NULL)
		return (0);

	elm1 = list->next;
	elm2 = list->next->next;

	while (elm1 && elm2 && elm2->next)
	{
		if (elm1 == elm2)
			return (1);
		elm1 = elm1->next;
		elm2 = elm2->next->next;
	}
	return (0);
}
