#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: first node.
 * @number: number to be inserted.
 *
 * Return: a pointer or Null.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;
	listint_t *previous = NULL;

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current != NULL && current->n <= number)
	{
		previous = current;
		current = current->next;
	}
	previous->next = new_node;
	new_node->next = current;

	return (new_node);
}
