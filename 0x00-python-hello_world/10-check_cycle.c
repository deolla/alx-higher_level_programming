#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: list to be checked.
 *
 * Return: 0 or 1 if failed.
 */
int check_cycle(listint_t *list)
{
	listint_t *op;
	listint_t *ops;

	op = list;
	ops = list;

	while (ops != NULL && ops->next != NULL)
	{
		op = op->next;
		ops = ops->next->next;

		if (op == ops)
		{
			return (1);
		}
	}
	return (0);
}
