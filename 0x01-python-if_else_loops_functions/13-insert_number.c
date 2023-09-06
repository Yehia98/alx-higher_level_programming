#include "lists.h"

/**
 * insert_node - inserts a node at a certain index.
 * @head: pointer to pointer of first node of listint_t list.
 * @number: integer to be included in new node.
 * Return: address of the new element or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *new2;
	listint_t *current;
	unsigned int i = 0;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (*head);
		free(new);
	}
	else
	{
		while (i < 4)
		{
			current = current->next;
			i++;
		}
		new2 = current->next;
		current->next = new;
		new->next = new2;
	}
	return (new);
}
