#include "lists.h"

/**
 * check_cycle - checks for loop in linked list
 * @head: head of the linked list
 * Return: 1
 */

int check_cycle(listint_t *head)
{
	listint_t *bad;
	listint_t *good;

	if (!head)
	{
		return (0);
	}
	bad = head;
	good = head->next;

	while (good && bad && good->next)
	{
		if (bad == good)
			return (1);
		bad = bad->next;
		good = good->next->next;
	}
	return (0);
}
