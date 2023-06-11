#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - reverses a singly-linked listint_t list
 * @head: first node of list to reverse pointer
 *
 * Return: reversed list head pointer
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;

	return (*head);
}
/**
 * is_palindrome - checks if the singly linked list is a palindrome
 * @head: linked list head pointer
 *
 * Return:	0 when the linked list isn't a palindrome
 *		1 when the linked list is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rv, *m;

	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;

	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;

	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rv = reverse_listint(&temp);
	m = rv;

	temp = *head;
	while (rv)
	{
		if (temp->n != rv->n)
			return (0);
		temp = temp->next;
		rv = rv->next;
	}
	reverse_listint(&m);
	return (1);
}
